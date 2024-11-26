from .lexer import Lexer
from .parser import Parser
from .interpreter import Interpreter
from kpi.models import KPI, AssetKPI  # Import the KPI model
from .models import Message
class Processor:
    def __init__(self):
        """
        Initializes the Processor without needing a config file.
        The expressions are now loaded from the KPI model in the database.
        """
        pass  # No need to load KPIs in the constructor anymore




    def process_message(self, message):
        """
        Interpret and process a single message with the corresponding KPI expression.
        :param message: The Message object containing the input value.
        :param kpi_name: The name of the KPI to fetch the expression for.
        """
        print("-------------------------IN PROCESSOR-------------------------------------")
        asset_kpis = AssetKPI.objects.select_related('kpi').all()
        print(asset_kpis)
        for asset_kpi in asset_kpis:
            print(f"Asset ID: {asset_kpi.asset_id}, Equation: {asset_kpi.kpi.expression}")
        expression = asset_kpi.kpi.expression  # Get the expression using the KPI name


        if message.value.isdigit():
            expression = expression.replace("ATTR", str(message.value))
        else:
            expression = expression.replace("ATTR", f'"{str(message.value)}"')

        # Compile and interpret the expression
        print("-------------------------IN LEXER-------------------------------------")

        lexer = Lexer(expression)
        print("-------------------------IN PARSER-------------------------------------")

        parser = Parser(lexer)
        print("-------------------------IN INTERPRETER-------------------------------------")

        interpreter = Interpreter(parser)

        # Evaluate the expression
        try:
            result = interpreter.interpret()
            print(f"Result for message {message.value} and KPI {expression}: {result}")
        except Exception as e:
            print(f"Error evaluating expression '{expression}' for KPI {expression}: {e}")

        return result
