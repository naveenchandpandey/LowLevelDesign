from ParkingLotService.models import Vehicle
from ParkingLotService.models.car import Car
from ParkingLotService.managers.slot_manager import SlotManager
from ParkingLotService.managers.parking_operations_manager import ParkingOperationsManager


class ParkingLotService:

    def __init__(self, floors, slots):
        slot_manager = SlotManager()
        parking_operation_manager = ParkingOperationsManager(slot_manager)
        for floor in range(floors):
            slot_manager.create_slots(floor, slots)
        print(SlotManager.slot_store)
        car: Vehicle = Car('DL-01-3615', 'white', 'SUV')
        print(slot_manager.get_available_slots())
        parking_operation_manager.park(car, 0, 1)
        print(slot_manager.get_available_slots())
        parking_operation_manager.release(0, 1)
        print(slot_manager.get_available_slots())
        for slot in SlotManager.slot_store[0]:
            print(SlotManager.slot_store[0][slot])


if __name__ == '__main__':
    parking_lot_service = ParkingLotService(1, 4)
