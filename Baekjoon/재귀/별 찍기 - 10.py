# 클론 코딩

def star(l, x, y):
    if l == 1:
        return
    dx, dx2 = x + (l//3), x + (l//3)*2
    dy, dy2 = y + (l//3), y + (l//3)*2
    for i in range(dx, dx2):
        for j in range(dy, dy2):
            stars[i][j] = ' '  # 가운데 별은 빈칸으로 만들기
    
    star(l//3, x, y)   # 1/3 작은 그룹에 대해서도 같은 작업들
    star(l//3, dx, y)
    star(l//3, dx2, y)
    star(l//3, x, dy)
    star(l//3, x, dy2)
    star(l//3, dx, dy)
    star(l//3, dx, dy2)
    star(l//3, dx2, dy2)
    star(l//3, dx2, dy)

n = int(input())
stars = [["*"]*n for _ in range(n)]
star(n,0,0)
for strs in stars:
    print(''.join(strs))