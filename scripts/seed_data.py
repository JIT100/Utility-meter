
from django.contrib.auth.models import User
from utility.models import Meter, Meter_Data


class LocalInitializer:
    """
    A utility class for initializing seed data in the database.

    This class provides methods to set up initial users, meters, and meter data in the database
    for testing or development purposes.

    Usage:
        init_client = LocalInitializer()
        init_client.execute()

    Attributes:
        None

    Methods:
        setup_users(): Sets up an initial admin user if it doesn't already exist.

        setup_meter(): Sets up initial meter objects with predefined labels if they don't already exist.

        setup_meter_data(): Sets up initial meter data objects for predefined meters and values if they don't already exist.

        execute(): Orchestrates the execution of setup methods in the desired order.

    Example:
        init_client = LocalInitializer()
        init_client.execute()

    """
    def setup_users(self):
        """
        Sets up an initial admin user if it doesn't already exist.
        
        If the admin user already exists, prints a message indicating it and skips the creation process.
        If the admin user doesn't exist, creates a new superuser with default credentials.
        """

        print("Setting up users...")
        try:
            user = User.objects.get(username="admin")
            print("Admin user already exists. Skipping...")
        except User.DoesNotExist:
            user = User.objects.create_superuser(username="admin", email="admin@localhost.com", password="1234")
            print("Admin user created.")

    def setup_meter(self):
        """
        Sets up initial meter objects with predefined labels if they don't already exist.
        
        If a meter with a predefined label already exists, prints a message indicating it and skips the creation process.
        If a meter with a predefined label doesn't exist, creates a new meter object with the label.
        """

        print("Setting up meter...")
        labels = ["Temperature", "Size","Radiation", "Speed"]

        for label in labels:
            capitalized_label = label.capitalize()
            try:
                meter = Meter.objects.get(label=capitalized_label)
                print(f"Meter with label '{capitalized_label}' already exists. Skipping...")
            except Meter.DoesNotExist:
                meter = Meter.objects.create(label=capitalized_label)
                print(f"Meter with label '{capitalized_label}' created.")
    
    def setup_meter_data(self):
        """
        Sets up initial meter data objects for predefined meters and values if they don't already exist.
        
        For each predefined meter and value combination, checks if a corresponding meter data object already exists.
        If the meter data object already exists, prints a message indicating it and skips the creation process.
        If the meter data object doesn't exist, creates a new meter data object for the combination.
        """

        print("Setting up meter data...")
        values = [20,30,50]
        labels = ["Temperature", "Size","Radiation", "Speed"]
        for label in labels:
            capitalized_label = label.capitalize()
            try:
                meter = Meter.objects.get(label=capitalized_label)
                for value in values:
                    if Meter_Data.objects.filter(value=value, meter=meter).exists():
                        print(f"Meter Data with the value of '{value}' already exists in {capitalized_label} meter. Skipping...")
                    else:
                        Meter_Data.objects.create(value=value, meter=meter)
                        print(f"Meter Data with the value of '{value}' created for {capitalized_label} meter.")
                
            except Meter.DoesNotExist:
                print(f"Meter with label '{capitalized_label}' doesn't exist.")

    def execute(self):
        """
        Orchestrates the execution of setup methods in the desired order.
        
        Calls the setup methods (setup_users, setup_meter, setup_meter_data) in sequence to initialize seed data in the database.
        Prints a success message upon successful execution.
        """

        self.setup_users()
        self.setup_meter()
        self.setup_meter_data()
        print("Successfully executed seed data!")


def run():
    init_client = LocalInitializer()
    init_client.execute()