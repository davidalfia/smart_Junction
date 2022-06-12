class Junction:
    def __init__(self, junction, cd, is_smart, *traffic_lights, **junction_map):
        self.name = junction
        self.from_cd = cd
        self.is_smart = is_smart
        self.junction_map = junction_map
        self.traffic_lights_list = []
        for t in traffic_lights:
            self.traffic_lights_list.append(t)

    def __str__(self):
        return f'Junction name {self.name} hit from {self.from_cd}  and is_smart = {self.is_smart}'

    def get_traffic_list(self):
        return self.traffic_lights_list

    def get_next_junction_by_cd(self, cd):
        return self.junction_map[cd]

    def add_traffic_light(self, traffic_light):
        self.traffic_lights_list.append(traffic_light)

    def set_priority_traffic_light_timer(self, traffic_light, new_timer):
        for t in self.traffic_lights_list:
            if t == traffic_light:
                t.set_timer(new_timer)

    def get_hit_from(self):
        return self.from_cd

    def get_traffic_light_and_next_cd_by_turn_choice(self, turn):
        for t in self.traffic_lights_list:
            if t.has(turn):
                return t, t.get_next_cd(turn)
        return None

    def set_is_smart(self, value):
        self.is_smart = value

    def get_is_smart(self):
        return self.is_smart


