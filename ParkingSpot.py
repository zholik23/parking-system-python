from constants import *
from abc import ABC


class ParkingSpot(ABC):
    def __init__(self, number, parking_spot_type):
        self.spot_number = number
        self.free = True
        self.__vehicle = None
        self.type = parking_spot_type

    def is_free(self):
        return self.free

    def assign_vehicle(self, vehicle):
        self.__vehicle = vehicle
        self.free = False

    def remove_vehicle(self):
        self.__vehicle = None
        self.free = True


class CarSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.CAR)





class VanSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.VAN)


class MotorbikeSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.MOTORBIKE)


class ElectricSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.ELECTRIC)

