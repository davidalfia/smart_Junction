class Controller:
    def __init__(self, **junction_map):
        self.junction_map = junction_map
        self.path_time = dict()
        self.path_time["AB"] = 10
        self.path_time["AC"] = 8
        self.path_time["AD"] = 6
        pass

    def add_junction_to_map(self,junction):
        self.junction_map.update(junction)

    def set_map_from_xl_file(self):
        pass

    def add_user_red_time(self):
        pass

    def add_user_path_time(self):
        pass

    def set_current_junction(self):
        pass

    def set_next_junction(self):
        pass

    def adjust_to_correct_traffic_light(self, choice_of_turn):
        pass

    def print_controller(self):
        for k, v in self.junction_map.items():
            print(k)
            v.print_junction()

    def get_junction_from_map(self,junction):
        return self.junction_map[junction]

    def get_path_time(self, pair):
        if pair in self.path_time.keys():
            return self.path_time[pair]
