from trafic_light import TrafficLight
from junction import Junction
from junction_file_module import list_of_junctions


class Controller:
    def __init__(self, **junction_map):
        self.junction_map = junction_map
        self.path_time = dict()
        self.path_time["AB"] = 1090
        self.path_time["AC"] = 996
        self.path_time["AD"] = 1052
        self.path_time["CD"] = 620
        self.path_time["DE"] = 320

    def add_junction_to_map(self, junction):
        self.junction_map.update(junction)

    def set_map_from_xl_file(self):
        pass

    def add_user_red_time(self):
        pass

    def get_junction_map(self):
        return self.junction_map

    def add_user_path_time(self):
        pass

    def set_current_junction(self):
        pass

    def set_next_junction(self):
        pass

    def adjust_to_correct_traffic_light(self, choice_of_turn):
        pass

    def get_junction_hit_from_by_junction_name_and_cardinal_direction(self, junction_name):
        return self.junction_map[junction_name]

    def get_junction_from_map(self, junction):
        return self.junction_map[junction]

    def get_path_time(self, pair):
        if pair in self.path_time.keys():
            return self.path_time[pair]

    def set_map(self):
        print("")
        # A2 = TrafficLight("A2", 100, 1, left="north", straight="east")
        # A3 = TrafficLight("A3", 100, 1, right="west", straight="south")
        # A4 = TrafficLight("A4", 100, 1, right="north", straight="west")
        # A5 = TrafficLight("A5", 100, 1, left="south")
        # A6 = TrafficLight("A6", 100, 1, right="east", straight="north")
        #
        # B1 = TrafficLight("B1", 100, 1, straight="south", left="east")
        # C1 = TrafficLight("C1", 100, 1, straight="north", right="east")
        #
        # D2 = TrafficLight("D1", 100, 1, straight="west", right="south")
        #
        # E2 = TrafficLight("E1", 100, 1, right="east", left="west")
        #
        # Aeast = Junction("A", "east", False, A1, A2, south="B", north="C", east="E", west=None)
        # Anorth = Junction("A", "north", False, A3, south="B", north="C", east="E", west=None)
        # Awest = Junction("A", "west", False, A4, A5, south="B", north="C", east="E", west=None)
        # Asouth = Junction("A", "south", False, A6, south="B", north="C", east="E", west=None)
        # A = [Aeast, Anorth, Awest, Asouth]
        # Bwest = Junction("B", "west", False, B1, south=None, north=None, east=None, west=None)
        # B = [Bwest]
        # Csouth = Junction("C", "south", False, C1, south=None, north=None, east="D", west=None)
        # C = [Csouth]
        # Deast = Junction("D", "east", False, D2, south="E", north=None, east=None, west=None)
        # D = [Deast]
        # Esouth = Junction("E", "south", False, E2, south=None, north=None, east=None, west=None)
        # E = [Esouth]

        # c = Controller(A=A,
        #                B=B,
        #                C=C,
        #                D=D,
        #                E=E)
        #
        # self.junction_map = {
        #     "A": A,
        #     "B": B,
        #     "C": C,
        #     "D": D,
        #     "E": E
        # }

    def build_users(self):
        pass

    def start_simulation(self, is_smart):
        pass

    def display_result(self):
        pass
