from enum import Enum
from . import Location
from . import Vehicle


class Slot:

    class Size(Enum):
        S = 'S'
        M = 'M'
        L = 'L'

    __id: int
    size: Size
    location: Location
    vehicle: Vehicle

    def __init__(self, slot_id, size, location, vehicle=None):
        self.__id = slot_id
        self.size = size
        self.location = location
        self.vehicle = vehicle

    def __str__(self):
        return f'ID: {self.__id}, Size: {self.size}, Location: {self.location}, Vehicle: {self.vehicle}'
