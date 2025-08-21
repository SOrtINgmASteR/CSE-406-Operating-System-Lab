# Disk scheduling - SSTF
request_sequence = [11, 34, 41, 50, 52, 69, 70, 114]
head = 50
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
