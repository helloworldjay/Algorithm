def solution(arrows):
    direction = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    visited, line = set([(0, 0)]), set()
    cnt = 0
    x, y = 0, 0
    for arrow in arrows:
        dx, dy = direction[arrow]
        newX = x + dx
        newY = y + dy
        if (newX, newY) in visited and ((x, y), (newX, newY)) not in line:
            cnt += 1
        visited.add((newX, newY))
        line.add(((x, y), (newX, newY)))
        line.add(((newX, newY), (x, y)))
        x, y = newX, newY
    return cnt
print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
