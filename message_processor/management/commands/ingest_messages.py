from django.core.management.base import BaseCommand
from message_processor.ingestor import DataIngestor
from message_processor.processor import Processor

class Command(BaseCommand):
    help = "Ingest messages from a file, process them, and save to the database"

    def handle(self, *args, **kwargs):
        file_path = 'message_processor/messages.txt'  # Path to your messages file
        config_path = 'message_processor/config.txt'
        # You no longer need to provide a config file, as the Processor will load expressions from the database

        # Initialize the Processor (no need for config_path)
        processor = Processor()

        # Create an instance of DataIngestor with the file path and processor
        data_ingestor = DataIngestor(file_path=file_path, processor=processor, config_path=config_path)

        # Process and save the messages
        data_ingestor.read_and_process()

        self.stdout.write(self.style.SUCCESS('Successfully ingested and processed messages into the database'))