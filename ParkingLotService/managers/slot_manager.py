from ..models import Slot
from ..models import Location
from ..services.slot_number_generator_factory import SlotNumberGeneratorFactory
from typing import Dict
from ..exceptions import InvalidFloorException
from ..exceptions import InvalidSlotException


class SlotManager:

    slot_store: Dict = dict()
    size: int

    def __init__(self):
        pass

    def create_slots(self, floor, size):
        slot_number_generator_factory = SlotNumberGeneratorFactory(SlotNumberGeneratorFactory.GeneratorTypes.SEQUENTIAL.value)
        slot_number_generator = slot_number_generator_factory.get_slot_number_generator(0)
        slot_map = {}
        for slot in range(0, size):
            current_slot = slot_number_generator.get_next_number()
            location = Location(f'{floor}_{current_slot}', floor)
            slot_map[current_slot] = Slot(current_slot, Slot.Size.M.value, location)
        self.slot_store[floor] = slot_map

    def remove_slots(self, floor, slot_id):
        if floor in self.slot_store:
            if slot_id in self.slot_store[floor]:
                del self.slot_store[floor][slot_id]
            else:
                raise InvalidSlotException("Provided slot is invalid")
        else:
            raise InvalidFloorException("Provided slot is invalid")

    def acquire_slot(self, floor, slot_id, vehicle):
        self.slot_store[floor][slot_id].vehicle = vehicle

    def release_slot(self, floor, slot_id):
        self.slot_store[floor][slot_id].vehicle = None

    def get_available_slots(self):
        available_slots = {}
        for floor in self.slot_store:
            available_slots[floor] = []
            for slot in self.slot_store[floor]:
                if not self.slot_store[floor][slot].vehicle:
                    available_slots[floor].append(slot)

        return available_slots
