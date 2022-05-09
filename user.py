class User:
    def __init__(self, name, cardinal_direction, priority, destination, source):
        self.name = name
        self.social_priority = priority
        self.current_Cardinal_Direction = cardinal_direction
        self.total_travel_time = 0
        self.dest = destination
        self.source = source

    def print(self):
        print(f'user {self.name} has priority of {self.social_priority}'
              f'and current direction is {self.current_Cardinal_Direction}')

    def get_social_priority(self):
        return self.social_priority

    def set_social_priority(self, new_social_priority):
        self.social_priority = new_social_priority

    def set_curr_cardinal_direction(self, new_cardinal_direction):
        self.current_Cardinal_Direction = new_cardinal_direction

    def get_curr_cardinal_direction(self):
        return self.current_Cardinal_Direction

    def add_to_travel_time(self, addition):
        self.total_travel_time += addition

    def get_cuurent_time(self):
        return self.total_travel_time

    def get_dest(self):
        return self.dest

    def get_source(self):
        return self.source
