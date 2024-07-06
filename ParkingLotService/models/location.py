class Location:

    __id: str
    floor: int

    def __init__(self, location_id, floor):
        self.__id = location_id
        self.floor = floor

    def __str__(self):
        return f'ID: {self.__id}, Floor: {self.floor}'
