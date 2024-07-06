from unittest import TestCase
from ParkingLotService.models import Vehicle
from ParkingLotService.models.car import Car
from ParkingLotService.managers.slot_manager import SlotManager
from ParkingLotService.managers.parking_operations_manager import ParkingOperationsManager


class CheckFreeSlots(TestCase):

    def test_available_slots(self):
        slot_manager = SlotManager()
        parking_operation_manager = ParkingOperationsManager(slot_manager)
        for floor in range(1):
            slot_manager.create_slots(0, 5)

        car: Vehicle = Car('DL', 'w', 'S')
        parking_operation_manager.park(car, 0, 1)
        available_slots = slot_manager.get_available_slots()[0]

        self.assertListEqual(available_slots, [2, 3, 4, 5])
