import string

with open("input_day3.txt") as f:
    lines = f.readlines()
    s = 0
    for i in range(0,len(lines),3):
        a_str = lines[i] 
        b_str = lines[i+1]
        c_str = lines[i+2]
        for j in a_str:
            if j in b_str and j in c_str:
                s = s + string.ascii_letters.index(j) + 1
                break
    print(s)

