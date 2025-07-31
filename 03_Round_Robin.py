class Process:
    def __init__(self, p_id, arrival_time, burst_time):
        self.p_id = p_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_burst_time = burst_time
        self.completion_time = 0
        self.turn_around_time = 0
        self.waiting_time = 0
        self.is_completed = False

# Input
n = int(input("Enter the number of processes: "))
quantum = int(input("Enter the time quantum: "))
processes = []

for i in range(n):
    at = int(input(f"Enter arrival time for process P{i + 1}: "))
    bt = int(input(f"Enter burst time for process P{i + 1}: "))
    processes.append(Process(f"P{i + 1}", at, bt))

# Sort by arrival time initially
processes.sort(key=lambda x: x.arrival_time)

ready_queue = []
current_time = 0
completed_processes = 0
visited = [False] * n  

# Add all processes that arrive at time 0
for i in range(n):
    if processes[i].arrival_time == 0:
        ready_queue.append(processes[i])
        visited[i] = True

while completed_processes < n:
    if not ready_queue:
        current_time += 1
        for i in range(n):
            if processes[i].arrival_time <= current_time and not visited[i]:
                ready_queue.append(processes[i])
                visited[i] = True
        continue

    current_process = ready_queue.pop(0)

    exec_time = min(current_process.remaining_burst_time, quantum)
    current_process.remaining_burst_time -= exec_time
    current_time += exec_time

    # Add newly arrived processes to the queue
    for i in range(n):
        if processes[i].arrival_time <= current_time and not visited[i]:
            ready_queue.append(processes[i])
            visited[i] = True

    if current_process.remaining_burst_time == 0:
        current_process.is_completed = True
        current_process.completion_time = current_time
        completed_processes += 1
    else:
        ready_queue.append(current_process)

# Calculate TAT and WT
for p in processes:
    p.turn_around_time = p.completion_time - p.arrival_time
    p.waiting_time = p.turn_around_time - p.burst_time

# Output
print("\nP-ID\tAT\tBT\tCT\tTAT\tWT")
for p in processes:
    print(f"{p.p_id}\t{p.arrival_time}\t{p.burst_time}\t{p.completion_time}\t{p.turn_around_time}\t{p.waiting_time}")

avg_wt = sum(p.waiting_time for p in processes) / n
print(f"\nAverage Waiting Time: {avg_wt:.2f}")
