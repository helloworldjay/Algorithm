from sys import stdin
input = stdin.readline
dp = {}
def recursive_w(a, b, c):
    if (a, b, c) in dp:
        return dp[(a, b, c)]
    elif a <= 0 or b <= 0 or c <= 0:
        dp[(a, b, c)] = 1
    elif a > 20 or b > 20 or c > 20:
        dp[(a, b, c)] = recursive_w(20, 20, 20)
    elif a < b and b < c:
        dp[(a, b, c)] = recursive_w(a, b, c-1) + recursive_w(a, b-1, c-1) - recursive_w(a, b-1, c)
    else:
        dp[(a, b, c)] = recursive_w(a-1, b, c) + recursive_w(a-1, b-1, c) + recursive_w(a-1, b, c-1) - recursive_w(a-1, b-1, c-1)
    return dp[(a, b, c)]
while True:
    x, y, z = map(int, input().split())
    if x == -1 and y == -1 and z == -1:
        break
    print(f"w({x}, {y}, {z}) = {recursive_w(x, y, z)}")