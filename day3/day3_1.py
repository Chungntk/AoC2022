import string

with open("input_day3.txt") as f:
    lines = f.readlines()
    s = 0
    for line in lines:
        if line != '':
            l = int(len(line.strip())/2)
            a_str = line[:l] 
            b_str = line[l:]
            
            for i in a_str:
                if i in b_str:
                    
                    s = s + string.ascii_letters.index(i) + 1
                    break
    print(s)

