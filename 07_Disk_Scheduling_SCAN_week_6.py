# Disk scheduling - SCAN
request_sequence = [11, 34, 41, 50, 52, 69, 70, 114]
head = 50
disk_size = 199  # Assuming disk ends at 0 and 199
direction = "left"

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
        total_movement += abs(head - up[0])  # Move from head to first right request
        total_movement += abs(up[0] - up[-1])  # Continue to last right request

    if len(up) > 0 and len(down) > 0:
        total_movement += abs(up[-1] - down[0])  # Reverse to first left request
        total_movement += abs(down[0] - down[-1])  # Continue to last left request

else:
    # First service all requests to the left
    for r in down:
        order.append(r)
    # Then service requests to the right
    for r in up:
        order.append(r)

    if len(down) > 0:
        total_movement += abs(head - down[0])  # Move from head to first left request
        total_movement += abs(down[0] - down[-1])  # Continue to last left request

    if len(down) > 0 and len(up) > 0:
        total_movement += abs(down[-1] - up[0])  # Reverse to first right request
        total_movement += abs(up[0] - up[-1])  # Continue to last right request

print("Order of servicing requests:", order)
print(f"Total head movement: {total_movement}")
