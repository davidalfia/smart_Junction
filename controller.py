from trafic_light import TrafficLight
from sub_junction import Junction
from roadUser import RoadUser
users = []
junction_map = {}
class Controller:
    def __init__(self,junction_map , users):
        self.junction_map = junction_map
        self.users = users
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

    def get_current_sub_junction(self, junction, cd):
        J = self.junction_map["A"]
        for s in J:
            if s.from_cd == cd:
                return s

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

    def build_users(self):
        pass

    def start_simulation(self, is_smart):
        pass

    def display_result(self):
        pass

    def get_junction_side(self,junction,current_cd):
        for j in junction:
            if j.from_cd == current_cd:
                return j

    def drive(self, is_smart):
        idx = 0
        for user in self.users:
            idx = 0
            choices = user.choices
            at_junction_name = user.get_current_junction_name()
            while at_junction_name is not user.dest:
                current_user_cd = user.get_curr_cardinal_direction()
                junction = self.junction_map[at_junction_name]
                turn_choice = choices[idx]
                junction_side = self.get_junction_side(junction, current_user_cd)
                traffic_Light, next_user_cd = junction_side.get_traffic_light_and_next_cd_by_turn_choice(turn_choice)
                user.set_curr_cardinal_direction(next_user_cd)
                prev_junction = at_junction_name
                at_junction_name = junction_side.get_next_junction_by_cd(next_user_cd)
                user.add_travel_time(self.path_time[prev_junction+at_junction_name])
                traffic_Light.push_user_to_traffic_light(user)
                traffic_Light.get_curr_timer_red(user, is_smart)
                traffic_Light.pop_user_from_traffic_light()
                user.set_current_junction(at_junction_name)
                idx = idx+1
                if idx == 3:
                    idx = 0

    def set_map(self):
        A1 = TrafficLight("A1", 100, 20, left="north", straight="east")
        A2 = TrafficLight("A2", 100, 20, right="south")
        A3 = TrafficLight("A3", 100, 20, right="west", straight="south")
        A4 = TrafficLight("A4", 100, 20, right="north", straight="west")
        A5 = TrafficLight("A5", 100, 20, left="south")
        A6 = TrafficLight("A6", 100, 20, right="east", straight="north")
        Aeast = Junction("A", "east", False, A1, A2, south="B", north="C", east="E", west=None)
        Anorth = Junction("A", "north", False, A3, south="B", north="C", east="E", west=None)
        Awest = Junction("A", "west", False, A4, A5, south="B", north="C", east="E", west=None)
        Asouth = Junction("A", "south", False, A6, south="B", north="C", east="E", west=None)
        A = [Aeast, Anorth, Awest, Asouth]

        B1 = TrafficLight("B1", 100, 20, left="south", right="north")
        B2 = TrafficLight("B2", 100, 20, straight="north", right="east")
        B3 = TrafficLight("B3", 100, 20, straight="south", left="east")
        Bwest = Junction("B", "west", False, B1, south=None, north="A", east=None, west=None)
        Bsouth = Junction("B", "south", False, B2, south=None, north="A", east=None, west=None)
        Bnorth = Junction("B", "north", False, B3, south=None, north="A", east=None, west=None)
        B = [Bwest, Bsouth, Bnorth]

        C1 = TrafficLight("C1", 100, 20, straight="north", right="east")
        C2 = TrafficLight("C3", 100, 20, left="south", right="north")
        C3 = TrafficLight("C2", 100, 20, straight="south", left="east")
        Csouth = Junction("C", "south", False, C3, south=None, north=None, east="D", west=None)
        Cwest = Junction("C", "west", False, C2, south=None, north=None, east="D", west=None)
        Cnorth = Junction("C", "north", False, C1, south=None, north=None, east="D", west=None)
        C = [Csouth, Cwest, Cnorth]

        D1 = TrafficLight("D1", 100, 20, left="south", straight="west")
        D2 = TrafficLight("D2", 100, 20, straight="east", right="south")
        D3 = TrafficLight("D3", 100, 20, right="east", left="west")
        Dwest = Junction("D", "west", False, D1, south="E", north=None, east=None, west=None)
        Deast = Junction("D", "east", False, D2, south="E", north=None, east=None, west=None)
        Dsouth = Junction("D", "south", False, D3, south="E", north=None, east=None, west=None)
        D = [Deast, Dwest, Dsouth]

        E1 = TrafficLight("E1", 100, 20, right="north", straight="west")
        E2 = TrafficLight("E2", 100, 20, right="east", left="west")
        E3 = TrafficLight("E2", 100, 20, straight="east", left="north")
        Ewest = Junction("E", "west", False, E1, south=None, north=None, east=None, west=None)
        Esouth = Junction("E", "south", False, E2, south=None, north=None, east=None, west=None)
        Eeast = Junction("E", "east", False, E3, south=None, north=None, east=None, west=None)
        E = [Esouth, Ewest, Eeast]

        F1 = TrafficLight("F1", 100, 20, left="north", straight="east")
        F2 = TrafficLight("F2", 100, 20, right="south")
        F3 = TrafficLight("F3", 100, 20, right="west", straight="south")
        F4 = TrafficLight("F4", 100, 20, right="north", straight="west")
        F5 = TrafficLight("F5", 100, 20, left="south")
        F6 = TrafficLight("F6", 100, 20, right="east", straight="north")
        Feast = Junction("F", "east", False, F1, F2, south=None, north="B", east="G", west=None)
        Fnorth = Junction("F", "north", False, F3, south=None, north="B", east="G", west=None)
        Fwest = Junction("F", "west", False, F4, F5, south=None, north="B", east="G", west=None)
        Fsouth = Junction("F", "south", False, F6, south=None, north="B", east="G", west=None)
        F = [Feast, Fnorth, Fwest, Fsouth]

        G1 = TrafficLight("G1", 100, 20, left="north", straight="east")
        G2 = TrafficLight("G2", 100, 20, right="south")
        G3 = TrafficLight("G3", 100, 20, right="west", straight="south")
        G4 = TrafficLight("G4", 100, 20, right="north", straight="west", left="south")
        G5 = TrafficLight("G5", 100, 20, right="east", straight="north", left="west")

        Geast = Junction("G", "east", False, G1, G2, south=None, north="H", east=None, west="F")
        Gnorth = Junction("G", "north", False, G3, south=None, north="H", east=None, west="F")
        Gwest = Junction("G", "west", False, G4, south=None, north="H", east=None, west="F")
        Gsouth = Junction("G", "south", False, G5, south=None, north="H", east=None, west="F")
        G = [Deast, Gnorth, Dwest, Dsouth]

        H1 = TrafficLight("H1", 100, 20, left="south", straight="west")
        H2 = TrafficLight("H2", 100, 20, straight="east", right="south")
        H3 = TrafficLight("H3", 100, 20, right="east", left="west")
        Hwest = Junction("H", "west", False, H1, south="G", north=None, east=None, west="B")
        Heast = Junction("H", "east", False, H2, south="G", north=None, east=None, west="B")
        Hsouth = Junction("H", "south", False, H3, south="G", north=None, east=None, west="B")
        H = [Heast, Hwest, Hsouth]

        self.junction_map = {
            "A": A,
            "B": B,
            "C": C,
            "D": D,
            "E": E,
            "F": F,
            "G": G,
            "H": H
        }

        choices1 = ["left", "right", "right"]
        choices2 = ["right"]
        u1 = RoadUser("David", "east", 1, "A", "E", choices1)
        u2 = RoadUser("Ran", "east", 2, "A", "E", choices1)
        u3 = RoadUser("Dana", "east", 3, "A", "E", choices1)
        u4 = RoadUser("Nir", "east", 4, "A", "E", choices1)
        u5 = RoadUser("Dov", "east", 5, "A", "E", choices1)
        u6 = RoadUser("Eran", "east", 6, "A", "E", choices1)
        u7 = RoadUser("Dor", "east", 7, "A", "E", choices1)
        u8 = RoadUser("Yam", "east", 8, "A", "E", choices1)
        self.users.append(u1)
        self.users.append(u2)
        self.users.append(u3)
        self.users.append(u5)
        self.users.append(u6)
        self.users.append(u7)
        self.users.append(u8)

        junction_map = self.junction_map
        users = self.users