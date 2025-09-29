# Page Replacemnt - FIFO
frames = []
page_sequence = [] 
page_faults = 0
page_hit = 0

frame_size = int(input("Enter Frame Size: "))
n = int(input("Enter number of sequence: "))
for i in range(n):
    x = input(f"Enter {i+1}st Sequence: ")
    page_sequence.append(x)

for page in page_sequence:
    if page not in frames:
        page_faults += 1
        if len(frames) < frame_size:
            frames.append(page)
        else:
            frames.pop(0)
            frames.append(page)
    else:
        page_hit += 1

print(f"Page Hits: {page_hit}")

print(f"Page Faults: {page_faults}")
