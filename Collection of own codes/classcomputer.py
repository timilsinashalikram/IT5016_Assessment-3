class Computer:
    def __init__(self, brand, model, ram_gb, storage_gb):
      #Set up the Computer object by adding in the brand, model, RAM, and storage details.
        self.brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.storage_gb = storage_gb
        self.is_on = False  # Initialize the is_on attribute to False

    def upgrade_ram(self, additional_ram_gb):
        # Upgrade RAM by installing more RAM.
        self.ram_gb += additional_ram_gb
        print(f"Upgraded RAM to {self.ram_gb}GB")

    def upgrade_storage(self, additional_storage_gb):
        # Upgrade storage by adding additional storage
        self.storage_gb += additional_storage_gb
        print(f"Upgraded storage to {self.storage_gb}GB")

    def __str__(self):
        # Custom string representation for the Computer object
        return f"{self.brand} {self.model}: RAM - {self.ram_gb}GB, Storage - {self.storage_gb}GB"

# Example usage:
my_computer = Computer("Apple", "MacBook Pro", 8, 256)
print(my_computer)

my_computer.upgrade_ram(8)
my_computer.upgrade_storage(256)
print(my_computer)
