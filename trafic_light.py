class TrafficLight:
    def __init__(self, name, red_timer, hit_from):
        self.name = name
        self.red_timer = red_timer
        self.green_timer = 1
        self.hit_from = hit_from
        self.traffic_light_directions = {}
        self.analyze_directions_map(hit_from)

    def get_curr_timer(self):
        return self.red_timer

    def set_timer(self, new_timer):
        self.red_timer = new_timer

    def get__cardinal_direction_by_turn_choice(self, turn_direction):
        return self.traffic_light_directions[turn_direction]

    def analyze_directions_map(self, hit_from):
        if hit_from == "west":
            self.traffic_light_directions = {"left": "north", "straight": "west", "right": "south"}
        elif hit_from == "north":
            self.traffic_light_directions = {"left": "west", "straight": "north", "right": "east"}
        elif hit_from == "south":
            self.traffic_light_directions = {"left": "west", "straight": "south", "right": "east"}
        elif hit_from == "east":
            self.traffic_light_directions = {"left": "south", "straight": "east", "right": "north"}

    def print_traffic_light(self):
        print(f'traffic_light {self.name} has current stop light timer of {self.timer}'
              f' and has directions: {self.traffic_light_directions}')


# t = TrafficLight("1", 8, left="north", right="south", straight="west")
