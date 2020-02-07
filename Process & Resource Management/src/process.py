from resource import Resource

class Process:
    def __init__(self, id, state, parent, priority):
        self.id = id            # process id
        self.state = state      # 0 - blocked, 1 - ready
        self.parent = parent    # parent's process id
        self.priority = priority
        self.children = []      # list of child process ids
        self.resources = []     # list of resource ids

    def create(self, id, priority, ready_list, pcb):
        new_proc = Process(id, 1, self.id, priority)
        pcb.append(new_proc)
        self.children.append(new_proc.id)
        ready_list[priority].append(new_proc.id)
        print("Process %d created" % new_proc.id)

    def destroy(self, child, ready_list, pcb):
        num_destroyed = 1

        for c in child.children:
            child.children.remove(c)
            num_destroyed += 1

        self.children.remove(child.id)

        if child.id in ready_list:
            ready_list[child.priority].remove(child.id)

        for resource in child.resources:
            if child.id in resource.waitlist:
                resource.waitlist.remove(child.id)

        del child.resources[:]
        pcb.remove(child)

        print("%d process(es) destroyed" % num_destroyed)

    def request(self, resource, ready_list):
        if resource.state == 1:
            resource.state = 0
            self.resources.append(resource.id)
            print("Resource %d allocated" % resource.id)
        else:
            self.state = 0
            resource.waitlist.append(self.id)
            ready_list.remove(self.id)
            print("Process %d blocked" % self.id)
            #scheduler();

    def release(self, resource, ready_list):
        this.resources.remove(resource.id)

        if len(resource.waitlist) == 0:
            resource.state = 0
        else:
            nextProc = resource.waitlist[0]
            ready_list.append(nextProc)
            nextProc.state = 1
            nextProc.resources.append(resource)

        print("Resource %d released" % resource.id)
