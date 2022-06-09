class RoadUser:
    def __init__(self, name, cardinal_direction, priority, start_at, dest):
        self.name = name
        self.cardinal_direction = cardinal_direction
        self.priority = priority
        self.travel_time = 0
        self.current_junction = start_at
        self.dest = dest;

    def __str__(self):
        return f'name = {self.name}, priority = {self.priority}, ' \
               f'current cd = {self.cardinal_direction} current time = {self.travel_time}  at junction : {self.current_junction}'

    def get_social_priority(self):
        return self.priority

    def get_user_dest(self):
        return self.dest;

    def set_social_priority(self, new_social_priority):
        self.priority = new_social_priority

    def set_curr_cardinal_direction(self, new_cardinal_direction):
        self.cardinal_direction = new_cardinal_direction

    def get_curr_cardinal_direction(self):
        return self.cardinal_direction

    def add_travel_time(self, addition):
        self.travel_time += addition

    def set_current_junction(self, junction):
        self.current_junction = junction

    def get_curr_travel_time(self):
        return self.travel_time

    def set_current_junction(self,junction):
        self.current_junction = junction

    def get_current_junction_name(self):
        return self.current_junction

    def restart_travel_time(self):
        self.travel_time = 0

