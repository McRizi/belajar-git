class Kendaraan:
    def __init__(self, brand):
        self.brand = brand

class Mobil(Kendaraan):
    def __init__(self, brand, model):
        super().__init__(brand)   # memanggil constructor Vehicle
        self.model = model

    def info(self):
        print(f"Mobil {self.brand} model {self.model}")