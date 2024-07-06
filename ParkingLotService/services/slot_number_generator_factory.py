from ParkingLotService.services.sequential_slot_number_generator import SequentialSlotNumberGenerator
from enum import Enum


class SlotNumberGeneratorFactory:

    class GeneratorTypes(Enum):
        SEQUENTIAL = 'sequential'

    def __init__(self, gen_type):
        self.gen_type = gen_type

    def get_slot_number_generator(self, starting_point):
        if self.gen_type == SlotNumberGeneratorFactory.GeneratorTypes.SEQUENTIAL.value:
            return SequentialSlotNumberGenerator(starting_point)
        else:
            return SlotNumberGeneratorFactory(None)


