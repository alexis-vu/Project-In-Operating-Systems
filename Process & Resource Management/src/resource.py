class Resource:
    def __init__(self, id, state, units):
        self.id = id            # resource id
        self.state = state      # 0 - allocated, 1 - free
        self.units = units      # number of units for resource
        self.waitlist = []      # waitlist of processes waiting for resource

    def hasUnits(self):
        return True if self.units > 0 else False
