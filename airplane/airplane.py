class Airplane:

    def num_seats(self):
        rows, seats = self.seating_plan()
        return len(rows) * len(seats)

    def seating_plan(self):
        pass