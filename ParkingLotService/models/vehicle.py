class Vehicle:

    __registration_no: int
    colour: str

    def __init__(self, registration_no, colour):
        self.__registration_no = registration_no
        self.colour = colour

    def get_registration_no(self):
        return self.__registration_no

    def get_colour(self):
        return self.colour

    def set_registration_no(self, registration_no):
        self.__registration_no = registration_no
