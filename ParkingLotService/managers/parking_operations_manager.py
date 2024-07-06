from ..managers.slot_manager import SlotManager


class ParkingOperationsManager:
    slot_manager: SlotManager

    def __init__(self, slot_manager):
        """

        :param slot_manager:
        """
        self.slot_manager = slot_manager

    def park(self, vehicle, floor, slot_id):
        self.slot_manager.acquire_slot(floor, slot_id, vehicle)

    def release(self, floor, slot_id):
        self.slot_manager.release_slot(floor, slot_id)
