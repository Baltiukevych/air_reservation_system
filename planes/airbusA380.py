from airplane import Airplane

class AirbusA380(Airplane):
    @staticmethod
    def get_name():
        return "AirbusA380"

    @staticmethod
    def seating_plan():
        return range(1, 41), "ABCDEGHIK"