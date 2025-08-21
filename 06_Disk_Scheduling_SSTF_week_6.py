# Disk scheduling - SSTF
n = int(input("Enter number of disk requests: "))
request_sequence = []
for i in range(n):
    req = int(input(f"Enter request {i+1}: "))
    request_sequence.append(req)
head = int(input("Enter initial head position: "))
requests = request_sequence.copy()
total_movement = 0
order = []

while requests:
    closest = requests[0]
    min_distance = abs(head - closest)
    for req in requests:
        distance = abs(head - req)
        if distance < min_distance:
            min_distance = distance
            closest = req

    total_movement += min_distance
    order.append(closest)
    head = closest
    requests.remove(closest)

print("Order of servicing requests:", order)
print(f"Total head movement: {total_movement}")
