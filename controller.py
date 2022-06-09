from trafic_light import TrafficLight
from junction import Junction


class Controller:
    def __init__(self, junction_map, users):
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
        pass

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
        choices = ["left","right","right"]
        idx = 0
        for user in self.users:
            at_junction_name = user.get_current_junction_name()
            print(f'start_at {at_junction_name}')
            while at_junction_name is not user.dest:
                current_user_cd = user.get_curr_cardinal_direction()
                junction = self.junction_map[at_junction_name]
                turn_choice = choices[idx]
                junction_side = self.get_junction_side(junction, current_user_cd)
                print(junction_side)
                traffic_Light,next_user_cd = junction_side.get_traffic_light_and_next_cd_by_turn_choice(turn_choice)
                user.set_curr_cardinal_direction(next_user_cd)
                at_junction_name = junction_side.get_next_junction_by_cd(next_user_cd)
                traffic_Light.push_user_to_traffic_light(user)
                traffic_Light.get_curr_timer_red(user, is_smart)
                traffic_Light.pop_user_from_traffic_light()
                print(f'turn {choices[idx]}')
                print(f'turn to cd  {next_user_cd}')
                user.set_current_junction(at_junction_name)
                idx = idx+1
                print(at_junction_name)
                print(user)