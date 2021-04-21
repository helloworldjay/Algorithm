def solution(dirs):
    trace = set()
    x, y = 0, 0
    for dir in dirs:
        temp_xy = (x, y)
        if dir == "U" and -5 <= y < 5:
            y += 1
        elif dir == "D" and -5 < y <= 5:
            y -= 1
        elif dir == "R" and -5 <= x < 5:
            x += 1
        elif dir == "L" and -5 < x <= 5:
            x -= 1
        if temp_xy != (x, y):
            trace.add((temp_xy, (x, y)))
            trace.add(((x, y), temp_xy))
    return len(trace)//2


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
