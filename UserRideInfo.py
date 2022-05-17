class UserRideInfo:
    def __init__(self, destination, source, travelType, numberOfJunctionsAlongPath):
        self.destination = destination
        self.source = source
        self.travelType = travelType
        self.numberOfJunctionsAlongPath = numberOfJunctionsAlongPath
        self._ETA = []

    def get_destination(self):
        return self.destination

    def get_source(self):
        return self.source

    def get_travelType(self):
        return self.travelType

    def get_numberOfJunctionsAlongPath(self):
        return self.numberOfJunctionsAlongPath

    def set_destination(self, destination):
        self.destination = destination

    def set_source(self, source):
        self.source = source

    def set_travelType(self, travelType):
        self.travelType = travelType

    def set_numberOfJunctionsAlongPath(self, num):
        self.numberOfJunctionsAlongPath = num
