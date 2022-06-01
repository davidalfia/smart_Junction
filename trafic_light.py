from queue import Queue
from roadUser import RoadUser


class TrafficLight:
    def __init__(self, name, red_timer, green_timer,**options):
        self.name = name
        self.red_timer = red_timer
        self.options = options
        self.green_timer = green_timer
        self.line = Queue()

    def get_curr_timer_red(self, priority, is_smart):
        if not is_smart:
            return self.red_timer
        else:
            return 100 - ((priority-1)*10)

    def set_curr_timer_green(self, new_timer):
        self.green_timer = new_timer

    def get__cardinal_direction_by_turn_choice(self, turn_direction):
        return self.options[turn_direction]

    def __str__(self):
        return (f'traffic_light {self.name} has current stop light timer of {self.red_timer} '
                f'and has directions: {self.options}')

    def push_user_to_traffic_light(self, road_user):
        print(f'traffic_light {self.name} got {road_user.name} in line')
        self.line.put_nowait(road_user)

    def pop_user_from_traffic_light(self):
        u = self.line.get_nowait()
        print(f'{u.name} passed {self.name} traffic_light')
        return u

    def get_options(self):
        return self.options

    def has_choice(self, turn):
        if turn in self.options.keys():
            return True
        return False

    def get_next_cd_by_turn(self, turn):
        return self.options[turn]

    def display_current_queue_size(self):
        print(self.line.qsize())
