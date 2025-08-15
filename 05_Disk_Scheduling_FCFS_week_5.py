# Disk scheduling - FCFS
request_sequence = [0, 16, 24, 43, 50, 82, 100, 140, 150, 170, 190, 199]
head = 50
idx = -1
for i in range(0, len(request_sequence)):
    if request_sequence[i] == head:
        idx = i
steps = (request_sequence[len(request_sequence) - 1] - request_sequence[0]) + (request_sequence[idx] - request_sequence[0])
print(f"Number of Steps: {steps}")
