# message_processor/ingestor.py
from datetime import datetime

import kpi
from message_processor.models import Message
from kpi.models import KPI, AssetKPI
from message_processor.processor import Processor
import time
import json


class DataIngestor:
    def __init__(self, file_path: str, processor: Processor, config_path: str):
        self.file_path = file_path
        self.processor = processor
        self.config_path = config_path

    def read_and_process(self):
        # Load KPIs into the database
        self.load_kpis_from_config()

        try:
            with open(self.file_path, 'r') as message_file:
                messages = [line.strip() for line in message_file if line.strip()]

            for i, message_line in enumerate(messages):
                try:
                    # Pass the raw JSON string to `Message.from_json`
                    message = Message.from_json(message_line)
                    Message.objects.create(
                        asset_id=message.asset_id,
                        attribute_id=message.attribute_id,  # Example, modify if needed
                        timestamp=message.timestamp,
                        value=message.value  # Processed value
                    )
                    print(f"Processing Line {i + 1}")

                    new_value = self.processor.process_message(message)

                    # Save the processed message to the database
                    Message.objects.create(
                        asset_id=message.asset_id,
                        attribute_id='output',  # Example, modify if needed
                        timestamp=datetime.now(),
                        value=new_value  # Processed value
                    )

                except json.JSONDecodeError as e:
                    print(f"Invalid JSON in line {i + 1}: {e}")
                except Exception as e:
                    print(f"Error processing line {i + 1}: {e}")

                time.sleep(5)  # Optional: Throttle processing

        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")


    def load_kpis_from_config(self):
        """
        Reads the configuration file to create KPI records.
        Each line in the config file represents a KPI with its name, expression, and description (optional).
        """
        try:
            with open(self.config_path, 'r') as config_file:
                for line in config_file:
                    line = line.strip()
                    if line:
                        # Assuming the config file format is: name, expression, optional description
                        parts = line.split(",")
                        if len(parts) >= 2:
                            name = parts[0].strip()
                            expression = parts[1].strip()
                            description = parts[2].strip() if len(parts) > 2 else None

                            # Create KPI object and save to the database
                            kpi = KPI.objects.create(
                                name=name,
                                expression=expression,
                                description=description
                            )
                            print(f"KPI created: {name} with expression: {expression}")
                        else:
                            print(f"Invalid KPI format: {line}")
        except FileNotFoundError:
            print(f"Configuration file not found at: {self.config_path}")
