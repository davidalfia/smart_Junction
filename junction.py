class Junction:
    def __init__(self, name, num_of_lanes, is_smart, *traffic_lights):
        self.name = name
        self.num_of_lanes = num_of_lanes
        self.traffic_lights_list = []
        for t in traffic_lights:
            self.traffic_lights_list.append(t)
        self.is_smart = is_smart

    def print_junction(self):
        print(f'Junction name {self.name} has {self.num_of_lanes} lanes and is_smart = {self.is_smart}')
        for t in self.traffic_lights_list:
            t.print_traffic_light()

    def add_traffic_light(self, traffic_light):
        self.traffic_lights_list.append(traffic_light)

    def set_priority_traffic_light_timer(self, traffic_light, new_timer):
        for t in self.traffic_lights_list:
            if t == traffic_light:
                t.set_timer(new_timer)

    def get_junction_name(self):
        return self.name
