with open("input_day6.txt") as f:
    rnk = 0
    marker = []
    for char in f.read():
        if len(marker) < 4:
            marker.append(char)
            rnk = rnk + 1
        else:
            if len(set(marker)) == len(marker) and rnk > 4:
                break
            else:
                marker = marker[1:]
                marker.append(char)
                rnk = rnk + 1
print(rnk)