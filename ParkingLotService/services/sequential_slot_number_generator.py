

class SequentialSlotNumberGenerator:
    starting_point: int

    def __init__(self, starting_point):
        self.starting_point = starting_point

    def get_next_number(self):
        self.starting_point += 1
        return self.starting_point


