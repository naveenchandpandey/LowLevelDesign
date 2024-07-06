from . import Vehicle
from enum import Enum


class Car(Vehicle):

    class CarType(Enum):
        LMV = 'LMV'
        SUV = 'SUV'

    type: CarType

    def __init__(self, registration_no, colour, car_type):
        super().__init__(registration_no, colour)
        self.type = car_type

    def __str__(self):
        return f'Registration No.: {self.get_registration_no()}, Colour: {self.colour}, Type: {self.type}'
