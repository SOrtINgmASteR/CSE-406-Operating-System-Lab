# Disk scheduling - SCAN
request_sequence = [11, 34, 41, 50, 52, 69, 70, 114]
head = 50
disk_size = 199  # Assuming disk ends at 0 and 199
direction = "up"  # "up" means moving towards higher cylinder numbers

requests = sorted(request_sequence)
idx = requests.index(head)
total_movement = 0
order = []

if direction == "up":
    # Move up to the end, then reverse
    up = [r for r in requests if r >= head]
    down = [r for r in requests if r < head][::-1]
    order = up + down
    total_movement += abs(head - up[-1])  # Move up
    if down:
        total_movement += abs(up[-1] - down[0])  # Reverse and move down
        total_movement += abs(down[0] - down[-1])  # Move down
else:
    # Move down to the start, then reverse
    down = [r for r in requests if r <= head][::-1]
    up = [r for r in requests if r > head]
    order = down + up
    total_movement += abs(head - down[0])  # Move down
    if up:
        total_movement += abs(down[0] - up[0])  # Reverse and move up
        total_movement += abs(up[0] - up[-1])  # Move up

print("Order of servicing requests:", order)
print(f"Total head movement: {total_movement}")