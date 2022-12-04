with open("input_day4.txt") as f:
    s = 0
    for line in f:
        p1, p2  = line.split(',')
        p1_start, p1_end = p1.split('-')
        p2_start, p2_end = p2.split('-')
        if ((int(p1_start) - int(p2_start))*(int(p1_end) - int(p2_end)) <= 0) or ((int(p1_start) - int(p2_start))*(int(p1_end) - int(p2_start)) <= 0) or ((int(p1_start) - int(p2_end))*(int(p1_end) - int(p2_end)) <= 0) :
            s = s + 1
    print(s)