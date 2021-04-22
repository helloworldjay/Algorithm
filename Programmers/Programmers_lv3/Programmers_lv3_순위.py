def solution(n, results):
    table = [[0 for _ in range(n)] for _ in range(n)]
    win, lost = 1, -1
    for winner, loser in results:
        table[winner-1][loser-1], table[loser-1][winner-1] = win, lost
    for me in range(n):
        losers = [index for index, cand in enumerate(table[me]) if cand == win]
        while losers:
            loser = losers.pop()
            for index, cand in enumerate(table[loser]):
                if cand == win and table[me][index] == 0:
                    table[me][index], table[index][me] = win, lost
                    losers.append(index)
    return len(["fixed" for i in range(n) if table[i].count(0) == 1])

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))