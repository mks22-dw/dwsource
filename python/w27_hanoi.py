def hanoi(num_disks, start, mid, end):
    if (num_disks == 1):
        print(start, 'to', end)
    else:
        hanoi(num_disks-1, start, end, mid)
        print(start, 'to', end)
        hanoi(num_disks-1, mid, start, end)
        
hanoi(5, 0, 1, 2)