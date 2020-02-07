from collections import OrderedDict
from resource import Resource
import copy

class Process:
    def __init__(self, id, state, parent, priority):
        self.id = id                    # process id
        self.state = state              # 0 - blocked, 1 - ready
        self.parent = parent            # parent's process id
        self.priority = priority        # process priority
        self.children = []              # list of child process ids
        self.resources = OrderedDict()  # list of resource, unit pairs

    def create(self, id, priority, ready_list, pcb, current_proc):
        current_proc = copy.deepcopy(current_proc)
        new_proc = Process(id, 1, self.id, priority)
        pcb.append(new_proc)
        self.children.append(new_proc.id)
        ready_list[priority].append(new_proc.id)
        print("Process %d created" % new_proc.id)

        if new_proc.priority > self.priority:
            current_proc = self.scheduler(ready_list)

    def destroy(self, child, ready_list, pcb, current_proc):
        num_destroyed = 1

        for c in child.children:
            child.children.remove(c)
            num_destroyed += 1

        self.children.remove(child.id)

        if child.id in ready_list[child.priority]:
            ready_list[child.priority].remove(child.id)

        for resource in child.resources:
            self.release(resource, ready_list, pcb, current_proc)

        pcb.remove(child)

        print("%d process(es) destroyed" % num_destroyed)

    def request(self, resource, units, ready_list, current_proc):
        if resource.state >= units and len(resource.waitlist) == 0:
            resource.state -= units
            self.resources[resource.id] = units
            print("Resource %d allocated" % resource.id)
        else:
            self.state = 0
            resource.waitlist[self.id] = units
            ready_list[self.priority].remove(self.id)
            print("Process %d blocked" % self.id)
            current_proc = self.scheduler(ready_list)

    def release(self, resource, units, ready_list, pcb, current_proc):
        del self.resources[resource.id]
        resource.state += units
        it = iter(resource.waitlist)
        while len(resource.waitlist) > 0 and resource.state > 0:
            next_proc_id = (next(it))[0]
            next_proc = pcb[next_proc_id]
            if resource.state >= units:
                resource.state -= units
                next_proc.resources[resource.id] = units
                next_proc.state = 1
                del resource.waitlist[next_proc_id]
                ready_list[next_proc.priority].append(next_proc_id)
            else:
                break

        print("Resource %d released" % resource.id)

        if nextProc.priority > self.priority:
            current_proc = self.scheduler(ready_list)

    def scheduler(self, ready_list):
        if len(ready_list[2]) > 0:
            current_proc = ready_list[2][0]
        elif len(ready_list[1]) > 0:
            current_proc = ready_list[1][0]
        else:
            current_proc = ready_list[0][0]

        print("Process %d running" % current_proc)
        return current_proc
