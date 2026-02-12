from abc import ABC, abstractmethod

class Kendaraan(ABC):
    
    @abstractmethod
    def nyalakan_mesin(self):
        pass

class Mobil(Kendaraan):
    def nyalakan_mesin(self):
        print("mobil dinyalakan dengan kunci atau tombol start")

class Motor(Kendaraan):
    def nyalakan_mesin(self):
        print("motor dinyalakan dengan starter kaki atau elektrik")

mobil1 = Mobil()
motor1 = Motor()

mobil1.nyalakan_mesin()
motor1.nyalakan_mesin()