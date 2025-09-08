# Question 2: Disk Scheduling Algorithm SCAN (Elevator)
n = int(input("Enter number of disk requests: "))
request_sequence = []
for i in range(n):
    req = int(input(f"Enter request {i+1}: "))
    request_sequence.append(req)
head = int(input("Enter initial head position: "))
disk_size = int(input("Enter disk size (last cylinder number): "))
direction = input("Enter direction (left/right): ").strip().lower()

requests = sorted(request_sequence)

down = []
up = []

for r in requests:
    if r < head:
        down.append(r)
    elif r > head:
        up.append(r)

down = down[::-1]

order = []
total_movement = 0

if direction == "right":
    for r in up:
        order.append(r)
    for r in down:
        order.append(r)

    if len(up) > 0:
        total_movement += abs(head - disk_size)  

    if len(up) > 0 and len(down) > 0:
        total_movement += abs(up[-1] - down[0])  
        total_movement += abs(down[0] - down[-1])  

elif direction == "left":
    for r in down:
        order.append(r)
    for r in up:
        order.append(r)

    if len(down) > 0:
        total_movement += abs(head - 0)

    if len(down) > 0 and len(up) > 0:
        total_movement += abs(0 - up[0]) 
        total_movement += abs(up[0] - up[-1])  

print("Order serving requests:", order)
print(f"Total Seek Time: {total_movement}")

