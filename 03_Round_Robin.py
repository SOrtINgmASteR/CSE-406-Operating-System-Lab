# Class for every process
class Process:
    def __init__(self, p_id, at, bt):
        self.p_id = p_id
        self.at = at
        self.bt = bt
        self.rbt = bt
        self.ct = 0
        self.tat = 0
        self.wt = 0
        self.is_done = False

# Input
n = int(input("Enter the number of processes: "))
quantum = int(input("Enter the time quantum: "))
processes = []

for i in range(n):
    at = int(input(f"Enter arrival time for process P{i + 1}: "))
    bt = int(input(f"Enter burst time for process P{i + 1}: "))
    processes.append(Process(f"P{i + 1}", at, bt))

# Sort by arrival time initially
processes.sort(key=lambda x: x.at)

current_time = 0
ready_queue = []
completed_processes = 0
visited = [False] * n  

# Add all processes that arrive at time 0
for i in range(n):
    if processes[i].at == 0:
        ready_queue.append(processes[i])
        visited[i] = True

while completed_processes < n:
    if not ready_queue:
        current_time += 1
        for i in range(n):
            if processes[i].at <= current_time and not visited[i]:
                ready_queue.append(processes[i])
                visited[i] = True
        continue

    current_process = ready_queue.pop(0)

    exec_time = min(current_process.rbt, quantum)
    current_process.rbt -= exec_time
    current_time += exec_time

    # Add newly arrived processes to the queue
    for i in range(n):
        if processes[i].at <= current_time and not visited[i]:
            ready_queue.append(processes[i])
            visited[i] = True

    if current_process.rbt == 0:
        current_process.is_done = True
        current_process.ct = current_time
        completed_processes += 1
    else:
        ready_queue.append(current_process)

# Calculate TAT and WT
for p in processes:
    p.tat = p.ct - p.at
    p.wt = p.tat - p.bt

# Output
print("\nP-ID\tAT\tBT\tCT\tTAT\tWT")
for p in processes:
    print(f"{p.p_id}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")

avg_wt = sum(p.wt for p in processes) / n
print(f"\nAverage Waiting Time: {avg_wt:.2f}")
