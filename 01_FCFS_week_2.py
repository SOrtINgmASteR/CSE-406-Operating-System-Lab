# Class for every process
class Process:
    def __init__(self, p_id, arrival_time, burst_time):
        self.p_id = p_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.ct = 0  # Completion Time
        self.tat = 0  # Turn Around Time
        self.wt = 0  # Waiting Time

# Input from user
n = int(input("Enter the number of processes: "))
processes = []

for i in range(n):
    at = int(input(f"Enter arrival time for process P{i}: "))
    bt = int(input(f"Enter burst time for process P{i}: "))
    processes.append(Process(f"P{i}", at, bt))


# Sort processes by arrival time (FCFS)
processes.sort(key=lambda x: x.arrival_time)


# Completion Time Calculation
processes[0].ct = processes[0].burst_time 
for i in range(1,4):
    processes[i].ct = processes[i - 1].ct + processes[i].burst_time


# Turn Around Time Calculation
for i in range(n):
    processes[i].tat = processes[i].ct - processes[i].arrival_time


# Waiting Time Calculation
for i in range(n):
    processes[i].wt = processes[i].tat - processes[i].burst_time


# Average waiting time
total_waiting_time = 0
for i in range(n):
    total_waiting_time += processes[i].wt
average_waiting_time = total_waiting_time / n


# Output
print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for p in processes:
    print(f"{p.p_id}\t{p.arrival_time}\t{p.burst_time}\t{p.ct}\t{p.tat}\t{p.wt}")

print(f"\nAverage Waiting Time: {average_waiting_time:.2f}")
