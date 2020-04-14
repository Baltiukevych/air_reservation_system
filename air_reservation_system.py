from pprint import pprint
from flight import Flight
# from planes import AirbusA380, Boeing777
from planes import *
from helpers import *


def make_flight():
    boeing = Boeing777()
    # print(boeing.num_seats())
airbus = AirbusA380()
# print()
# print(boeing.get_name())
f = Flight("LO127", boeing)
f.allocate_passenger("Jaroslaw K.", "1A")
f.allocate_passenger("Lech K.", "12B")
f.allocate_passenger("Zbiegniew K.", "22G")
f.relocate_passenger("1A", "1C")
f.relocate_passenger("12B", "11B")
# print(f.flight_number)
# print(f.get_airline())
# print(f.get_number())
# print(f.get_airplane_model())
pprint(f.seats)
# print(f.get_airplane_model())
f.print_cards(card_printer)
card_printer("Viktoriia Baltiukevych", "12C", "Airbus A380", "BA234")
card_printer("Viktoriia Baltiukevych", "12C", "Airbus A380", "BA234")
card_printer("Viktoriia Baltiukevych", "12C", "Airbus A380", "BA234")

make_flight()
