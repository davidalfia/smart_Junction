from queue import Queue
from roadUser import RoadUser


class TrafficLight:
    def __init__(self, name, red_timer, green_timer, **options):
        self.name = name
        self.red_timer = red_timer
        self.options = options
        self.green_timer = green_timer
        self.line = Queue()

    def get_curr_timer_red(self):
        return self.red_timer

    def get_curr_timer_green(self):
        return self.green_timer

    def set_curr_timer_red(self, new_timer):
        self.red_timer = new_timer

    def set_curr_timer_green(self, new_timer):
        self.green_timer = new_timer

    def get__cardinal_direction_by_turn_choice(self, turn_direction):
        return self.options[turn_direction]

    def __str__(self):
        return (f'traffic_light {self.name} has current stop light timer of {self.red_timer} '
                f'and has directions: {self.options}')

    def pop_from_traffic_light(self,road_user):
        self.line.put_nowait(road_user)

    def push_to_traffic_light(self):
        return self.line.get_nowait()

    def get_options(self):
        return self.options

    def has_choice(self, turn):
        if turn in self.options.keys():
            return True
        return False

    def get_next_cd_by_turn(self, turn):
        return self.options[turn]
