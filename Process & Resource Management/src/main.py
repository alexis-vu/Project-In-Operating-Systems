from process import Process
from resource import Resource

MAX_PROCESSES = 16
MAX_RESOURCES = 4
RL_LEVELS = [0, 1, 2]

# required data structures: PCB, RCB, RL
pcb = []
rcb = []
ready_list = {}

# parallel array to track allocation of procceses
allocated_proc = []

def init():
    global pcb
    global rcb
    global ready_list
    global allocated_proc

    if len(pcb) > 0:
        del pcb[:]

    if len(rcb) > 0:
        del rcb[:]

    if len(ready_list) > 0:
        ready_list.clear()

    if len(allocated_proc) > 0:
        del allocated_proc[:]

    pcb = [] * MAX_PROCESSES

    rcb = [None] * MAX_RESOURCES
    for i in range (0, MAX_RESOURCES):
        rcb[i] = Resource(i, 1, 0)
        rcb[i].units = 1 if i == 0 else i

    ready_list = {key: [] for key in RL_LEVELS}
    allocated_proc = [-1] * MAX_PROCESSES

    first_proc = Process(0, 1, None, 0)
    pcb.append(first_proc)
    ready_list[first_proc.priority].append(0)

def main():
    global pcb
    global rcb
    global ready_list

    print("Initializing system...")
    init()
    print("Process 0 created")
    print("Current pcb:"),
    print(pcb)

    print("\nCreating process: ")
    pcb[0].create(1, 0, ready_list, pcb)
    print("Current pcb:"),
    print(pcb)
    print("Current ready list:"),
    print(ready_list)

    print("\nDestroying process 1...")
    pcb[0].destroy(pcb[1], ready_list, pcb)
    print("Current pcb:"),
    print(pcb)
    print("Current ready list:"),
    print(ready_list)

if __name__ == '__main__':
    main()
