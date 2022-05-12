class RoadUser:
    def __init__(self, name, cardinal_direction, priority, travelTime):
        self.name = name
        self.cardinal_direction = cardinal_direction
        self.priority = priority
        self.travelTime = travelTime

    def get_social_priority(self):
        return self.priority

    def set_social_priority(self, new_social_priority):
        self.priority = new_social_priority

    def set_curr_cardinal_direction(self, new_cardinal_direction):
        self.cardinal_direction = new_cardinal_direction

    def get_curr_cardinal_direction(self):
        return self.cardinal_direction

    def add_travel_time(self, addition):
        self.travelTime += addition

    def get_curr_travel_time(self):
        return self.travelTime
