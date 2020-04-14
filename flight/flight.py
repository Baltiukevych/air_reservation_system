class Flight:
    def __init__(self, flight_number, plane):
        self.flight_number = flight_number
        self.plane = plane

        rows, letters = self.plane.seating_plan()
        self.seats = [None] + [{letter: None for letter in letters} for _ in rows]

    def get_airline(self):
        return self.flight_number[:2]

    def get_number(self):
        return self.flight_number[2:]

    def get_airplane_model(self):
        return self.plane.get_name()

    def _parse_seat(self, seat="12C"):
        rows, letters = self.plane.seating_plan()

        letter = seat[-1]

        if letter not in letters:
            raise ValueError(f"Invalid seat letter {letter}")

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat number {row_text}")

        if row not in rows:
            raise ValueError(f"Row {row}is out of range")

        return row, letter

    def allocate_passenger(self, passenger="Jan K.", seat="12C"):
        row, letter = self._parse_seat(seat)

        if self.seats[row][letter] is not None:
            raise ValueError(f"Seat {seat} is already occupied.")

        self.seats[row][letter] = passenger

    def relocate_passenger(self, seat_from, seat_to):
        row_from, letter_from = self._parse_seat(seat_from)
        if self.seats[row_from][letter_from] is None:
            raise ValueError(f"No passenger on the{seat_from} seat.")

        row_to, letter_to = self._parse_seat(seat_to)

        if self.seats[row_to][letter_to] is not None:
            raise ValueError(f"Seat{seat_to}is already occupied.")
        self.seats[row_to][letter_to] = self.seats[row_from][letter_from]
        self.seats[row_from][letter_from] = None

    def get_empty_seats(self):
        return sum(sum(1 for seat in row.values() if seat is None)
                   for row in self.seats
                   if row is not None)

    def print_cards(self, c_printer):
        passengers = self.get_passengers()

        for passengers, seat in passengers:
            c_printer(passengers, seat, self.get_airplane_model(), self.flight_number)

    def get_passengers(self):
        passengers = []
        rows, letters = self.plane.seating_plan()

        for row in rows:
            for letter in letters:
                passenger = self.seats[row][letter]
                if passenger is not None:
                    passengers_data = passenger, f"{row}{letter}"
                    passengers.append(passengers_data)
        return passengers