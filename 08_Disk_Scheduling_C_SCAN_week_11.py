# Disk scheduling: C-SCAN
n = int(input("Enter number of disk requests: "))
# request_sequence = [176, 79, 64, 90, 21, 39]
request_sequence = []
for i in range(n):
    req = int(input(f"Enter request {i+1}: "))
    request_sequence.append(req)
head = int(input("Enter initial head position: "))
direction = input("Enter direction (left/right): ").strip().lower()

requests = sorted(request_sequence)

total_movement = 0
execution_order = []

if direction == "left":
    left_segment = [req for req in requests if req <= head]
    right_segment = [req for req in requests if req > head]
    execution_order = left_segment[::-1] + right_segment[::-1]

    total_movement += (head - requests[0])
    total_movement += (requests[-1] - requests[0])
    idx = -1
    for i in range(n):
        if requests[i] > head:
            idx = i
            break
    if idx != -1:
        total_movement += (requests[-1] - requests[idx])

else:
    right_segment = [req for req in requests if req >= head]
    left_segment = [req for req in requests if req < head]
    execution_order = right_segment + left_segment

    total_movement += (requests[-1] - head)
    total_movement += (requests[-1] - requests[0])
    idx = -1
    for i in range(n):
        if requests[i] > head:
            idx = i - 1
            break
    if idx != -1:
        total_movement += (requests[idx] - requests[0])
    else:
        total_movement += (requests[-1] - requests[0])

print(f"Request execution order: ", end="")
if execution_order:
    for e in execution_order:
        print(f"{e} ", end="")
print()

print(f"Total head movement: {total_movement}")