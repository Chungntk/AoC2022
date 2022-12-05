l = [
    ["N", "R", "J", "T", "Z", "B", "D", "F"][::-1],
    ["H", "J", "N", "S", "R"][::-1],
    ["Q", "F", "Z", "G", "J", "N", "R", "C"][::-1],
    ["Q", "T", "R", "G", "N", "V", "F"][::-1],
    ["F", "Q", "T", "L"][::-1],
    ["N", "G", "R", "B", "Z", "W", "C", "Q"][::-1],
    ["M", "H", "N", "S", "L", "C", "F"][::-1],
    ["J", "T", "M", "Q", "N", "D"][::-1],
    ["S", "G", "P"][::-1],
]

with open("input_day5.txt") as f:
    for line in f:
        text = line.split()
        move, fr, to = int(text[1]), int(text[3]) - 1, int(text[5]) - 1
        for i in l[fr][-move:]:
            l[to].append(i)
            l[fr].pop()

    top_stack = []
    for crate in l:
        top_stack.append(crate.pop())
    print("".join(top_stack))
