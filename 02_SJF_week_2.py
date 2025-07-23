# Class for every process
class Process:
    def __init__(self, p_id, arrival_time, burst_time):
        self.p_id = p_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.ct = 0 
        self.tat = 0
        self.wt = 0
        self.visited = False

# Input Processes
n = int(input("Enter the number of processes: "))
processes = []

for i in range(n):
    at = int(input(f"Enter arrival time for process P{i + 1}: "))
    bt = int(input(f"Enter burst time for process P{i + 1}: "))
    processes.append(Process(f"P{i + 1}", at, bt))


#  Sort processes by arrival time
processes.sort(key=lambda x: x.arrival_time)


current_time = 0
completed = 0

# Completion Time Calculation
while completed < n:
    idx = -1
    min_bt = float('inf')
    for i in range(n):
        if not processes[i].visited and processes[i].arrival_time <= current_time:
            if processes[i].burst_time < min_bt:
                min_bt = processes[i].burst_time
                idx = i
            elif processes[i].burst_time == min_bt:
                if processes[i].arrival_time < processes[idx].arrival_time:
                    idx = i

    if idx == -1:
        current_time += 1
    else:
        processes[idx].ct = current_time + processes[idx].burst_time
        current_time = processes[idx].ct
        processes[idx].visited = True
        completed += 1


# Turn Around Time Calculation
for i in range(n):
    processes[i].tat = processes[i].ct - processes[i].arrival_time


# Waiting Time Calculation
for i in range(n):
    processes[i].wt = processes[i].tat - processes[i].burst_time


# Average waiting time
total_waiting_time = sum(p.wt for p in processes)
average_waiting_time = total_waiting_time / n


# Output
print("\nP-id\tAT\tBT\tCT\tTAT\tWT")
for p in processes:
    print(f"{p.p_id}\t{p.arrival_time}\t{p.burst_time}\t{p.ct}\t{p.tat}\t{p.wt}")

print(f"\nAverage Waiting Time: {average_waiting_time:.2f}")
