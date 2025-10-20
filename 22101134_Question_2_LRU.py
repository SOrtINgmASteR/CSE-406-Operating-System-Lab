# Name - Noor Mohammed Priom
# ID - 22101134
# Question 2: Page Replacement - LRU
page_reference = [] 
frame = []
page_hit = 0
page_faults = 0

frame_size = int(input("Frame Size: "))
n = int(input("Number of sequence: "))
for i in range(n):
    x = input(f"Enter {i+1}st Sequence: ")
    page_reference.append(x)

for page in page_reference:
    if page not in frame:
        page_faults += 1
        print("Miss: ")
        if len(frame) == frame_size:
            frame.pop(0)
            frame.append(page)
        else:
            frame.append(page)
        
    else:
        page_hit += 1
        print("Hit: ")
        frame.remove(page)
        frame.append(page)  
    
    # The frame is printed in least recently used order
    print(f"Frame: {frame}")

print(f"Page Hits: {page_hit}")
print(f"Page Faults: {page_faults}")


'''
Input: Frame Sequence
10
7
0
1
2
0
3
0
4
2
3
'''