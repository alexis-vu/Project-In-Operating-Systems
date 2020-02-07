from collections import OrderedDict
class Resource:
    def __init__(self, id, inventory):
        self.id = id                    # resource id
        self.inventory = inventory      # number of units
        self.state = inventory          # number of leftover units
        self.waitlist = OrderedDict()   # waitlist of process, unit pairs
