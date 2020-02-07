#from process import Process
from resource import Resource
from collections import OrderedDict
import fileinput

MAX_PROCESSES = 16
MAX_RESOURCES = 4
RL_LEVELS = [0, 1, 2]

# required data structures: PCB, RCB, RL
pcb = []
rcb = []
ready_list = OrderedDict()
current_proc = None

def init():
    global pcb
    global rcb
    global ready_list
    global current_proc

    if len(pcb) > 0:
        del pcb[:]

    if len(rcb) > 0:
        del rcb[:]

    if len(ready_list) > 0:
        ready_list.clear()

    pcb = [None] * MAX_PROCESSES

    rcb = [None] * MAX_RESOURCES
    for i in range (0, MAX_RESOURCES):
        rcb[i] = Resource(i, 0)
        rcb[i].inventory = 1 if i == 0 else i
        rcb[i].state = rcb[i].inventory

    ready_list = {key: [] for key in RL_LEVELS}

    first_proc = Process(0, 1, None, 0)
    pcb[0] = first_proc
    ready_list[first_proc.priority].append(0)
    print("Process 0 created")

def timeout():
    global ready_list

    if len(ready_list[0]) > 0:
        proc = ready_list[0][0]
        del ready_list[0][0]
        ready_list[0].append(proc)
    elif len(ready_list[1]) > 0:
        proc = ready_list[1][0]
        del ready_list[1][0]
        ready_list[1].append(proc)
    else:
        proc = ready_list[2][0]
        del ready_list[2][0]
        ready_list[2].append(proc)

class Process:
    def __init__(self, id, state, parent, priority):
        self.id = id                    # process id
        self.state = state              # 0 - blocked, 1 - ready
        self.parent = parent            # parent's process id
        self.priority = priority        # process priority
        self.children = []              # list of child process ids
        self.resources = OrderedDict()  # list of resource, unit pairs

    def create(self, id, priority):
        new_proc = Process(id, 1, self.id, priority)
        pcb[id] = new_proc
        self.children.append(new_proc.id)
        ready_list[priority].append(new_proc.id)
        print("Process %d created" % new_proc.id)

        if new_proc.priority > self.priority:
            self.scheduler()

    def destroy(self, child):
        num_destroyed = 1

        for c in child.children:
            child.children.remove(c)
            num_destroyed += 1

        self.children.remove(child.id)

        if child.id in ready_list[child.priority]:
            ready_list[child.priority].remove(child.id)

        for resource in child.resources:
            self.release(resource, ready_list, pcb, current_proc)

        pcb[child.id] = None

        print("%d process(es) destroyed" % num_destroyed)

    def request(self, resource, units):
        if resource.state >= units and len(resource.waitlist) == 0:
            resource.state -= units
            self.resources[resource.id] = units
            print("Resource %d allocated" % resource.id)
        else:
            self.state = 0
            resource.waitlist[self.id] = units
            ready_list[self.priority].remove(self.id)
            print("Process %d blocked" % self.id)
            self.scheduler()

    def release(self, resource, units):
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

            if next_proc.priority > self.priority:
                self.scheduler()

        print("Resource %d released" % resource.id)



    def scheduler(self):
        global current_proc

        if len(ready_list[2]) > 0:
            current_proc = ready_list[2][0]
        elif len(ready_list[1]) > 0:
            current_proc = ready_list[1][0]
        else:
            current_proc = ready_list[0][0]

        print("Process %d running" % current_proc)

def main():
    global pcb
    global rcb
    global ready_list
    global current_proc

    for input in fileinput.input():
        input = input.rstrip()
        command = input.split(" ")

        if command[0] == 'cr':
            if command[1] == None:
                continue
            else:
                if None not in pcb:
                    print("error")
                    continue
                else:
                    child_id = pcb.index(None)
                    priority = int(command[1])

                    if priority < 0 or priority > 2:
                        print("error")
                        continue

                    pcb[current_proc].create(child_id, priority)
        elif command[0] == 'de':
            if command[1] == None:
                continue
            else:
                child_id = int(command[1])
                if child_id not in pcb[current_proc].children:
                    print("error")
                    continue
                else:
                    pcb[current_proc].destroy(pcb[child_id])
        elif command[0] == 'rq':
            if command[1] == None or command[2] == None:
                continue
            else:
                r = int(command[1])
                u = int(command[2])

                if current_proc == 0:
                    print("error")
                    continue
                elif r > 3 or r < 0:
                    print("error")
                    continue
                elif r in pcb[current_proc].resources.keys():
                    print("error")
                    continue
                else:
                    pcb[current_proc].request(rcb[r], u)
        elif command[0] == 'rl':
            if command[1] == None or command[2] == None:
                continue
            else:
                r = int(command[1])
                u = int(command[2])

                if r > 0 or r < 0:
                    continue
                elif r not in pcb[current_proc].resources.keys():
                    print("error")
                    continue
                else:
                    pcb[current_proc].release(rcb[r], u)
        elif command[0] == 'to':
            timeout()
        elif command[0] == 'in':
            init()
            current_proc = 0
        elif command[0] == 'q':
            break
        else:
            continue

if __name__ == '__main__':
    main()
