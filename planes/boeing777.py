from airplane import Airplane
class Boeing777(Airplane):
    @staticmethod
    def get_name():
        return "Boeing 777"

    @staticmethod
    def seating_plan():
        return range(1, 23), "ABCDEG"

