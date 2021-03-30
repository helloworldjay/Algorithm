from sys import stdin
input = stdin.readline
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
paper_count = [0, 0]
def is_same_color(x:int, y:int, K:int) -> bool:
    paper_color = paper[x][y]
    for i in range(x, x+K):
        for j in range(y, y+K):
            if paper[i][j] != paper_color: return False
    return True
def check_paper(x, y, K):
    if is_same_color(x,y,K): paper_count[paper[x][y]] += 1
    else:
        half = K//2
        xx = x + half
        yy = y + half
        check_paper(x, y, half)
        check_paper(xx, y, half)
        check_paper(x, yy, half)
        check_paper(xx, yy, half)
check_paper(0, 0, N)
for i in range(2):
    print(paper_count[i])