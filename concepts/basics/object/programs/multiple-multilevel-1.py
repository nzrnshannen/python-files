class Device:
    def __init__(self, brand):
        self.brand = brand

class SmartAppliance(Device):
    def __init__(self, brand, power_rating):
        super().__init__(brand)
        self.power_rating = power_rating

class WifiCapable:
    def connect_to_wifi(self, network):
        print(f"{self.brand} device connected to {network}.")

class SmartWashingMachine(SmartAppliance, WifiCapable):
    def __init__(self, brand, power_rating):
        super().__init__(brand, power_rating)

    def start_wash(self):
        print(f"Starting wash cycle... Using {self.power_rating}")
