with open("input_day2.txt") as f:
    lines = f.readlines()
    guide = []
    s = 0
    for line in lines:
        u, me = line.split()
        if u == 'A' and me == 'X':
            s = s + 3 + 0
        if u == 'A' and me == 'Y':
            s = s + 1 + 3
        if u == 'A' and me == 'Z':
            s = s + 2 + 6
        if u == 'B' and  me == 'X':
            s = s + 1 + 0
        if u == 'B' and  me == 'Y':
            s = s + 2 + 3
        if u == 'B' and me == 'Z':
            s = s + 3 + 6
        if u == 'C' and me == 'X':
            s = s + 2 + 0
        if u == 'C' and me == 'Y':
            s = s + 3 + 3
        if u == 'C' and me == 'Z':
            s = s + 1 + 6
    print(s)
        
        # guide.append((u,me))
    
        
