class process:
    def __init__(self, p_id, arrival_time, burst_time):
        self.p_id = p_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.ct = 0
        self.tat = 0
        self.wt = 0

processes = []
processes.append(process("p0", 0, 4))
processes.append(process("p1", 2, 3))
processes.append(process("p2", 3, 2))
processes.append(process("p3", 5, 1))

for p in processes:
    print(f"{p.p_id} {p.arrival_time} {p.burst_time}")
print("\n")

# Completion Time Calculation
processes[0].ct = processes[0].burst_time 
for i in range(1,4):
    processes[i].ct = processes[i - 1].ct + processes[i].burst_time

# Turn Around Time Calculation
for i in range(0,4):
    processes[i].tat = processes[i].ct - processes[i].arrival_time

# Wating Time Calculation
for i in range(0,4):
    processes[i].wt = processes[i].tat - processes[i].burst_time

# Average waiting Time Calculation
total_waiting_time = 0
for i in range(4):
    total_waiting_time += processes[i].wt
average_waiting_time = total_waiting_time / 4
# print(f"{total_waiting_time}")

for p in processes:
    print(f"{p.p_id} {p.arrival_time} {p.burst_time} {p.ct} {p.tat} {p.wt}")
print(f"Average Waiting Time: {average_waiting_time}")
