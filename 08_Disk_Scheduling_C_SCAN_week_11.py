# Disk scheduling: C-SCAN
n = int(input("Enter number of disk requests: "))
request_sequence = []
for i in range(n):
    req = int(input(f"Enter request {i+1}: "))
    request_sequence.append(req)
head = int(input("Enter initial head position: "))
direction = input("Enter direction (left/right): ").strip().lower()

requests = sorted(request_sequence)

total_movement = 0

if direction == "left":
    total_movement += (head - requests[0])
    total_movement += (requests[-1] - requests[0])
    idx = -1
    for i in range(n):
        if requests[i] > head:
            idx = i
            break
    total_movement += (requests[-1] - requests[idx])

else:
    total_movement += (requests[-1] - head)
    total_movement += (requests[-1] - requests[0])
    idx = -1
    for i in range(n):
        if requests[i] > head:
            idx = i - 1
            break
    total_movement += (requests[idx] - requests[0])

print(f"Total head movement: {total_movement}")


'''
Input
6
176
79
64
90
21
39
50
'''