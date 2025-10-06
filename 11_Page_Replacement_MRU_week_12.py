# Page Replacement - MRU
frame = []
page_sequence = [] 
page_faults = 0
page_hit = 0

frame_size = int(input("Enter Frame Size: "))
n = int(input("Enter number of sequence: "))
for i in range(n):
    x = input(f"Enter {i+1}st Sequence: ")
    page_sequence.append(x)

for page in page_sequence:
    if page not in frame:
        page_faults += 1
        print("Miss: ")
        if len(frame) == 4:
            frame.pop(len(frame) - 1)
            frame.append(page)
        else:
            frame.append(page)
        
    else:
        page_hit += 1
        print("Hit: ")
        frame.remove(page)
        frame.append(page)  
    print(frame)     

print(f"Page Hits: {page_hit}")
print(f"Page Faults: {page_faults}")

print(f"Page Fault Ratio: {(page_faults / len(page_sequence)) * 100}")
print(f"Page Hit Ratio: {(page_hit / len(page_sequence)) * 100}")

'''
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
0
'''