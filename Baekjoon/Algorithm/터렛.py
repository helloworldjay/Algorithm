from sys import stdin

input = stdin.readline
T = int(input())
for _ in range(T):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())
    distance = (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2
    if distance == 0 and r_1 == r_2:
        print(-1)
    elif distance == (r_1 + r_2) ** 2 or distance == (r_1 - r_2) ** 2:
        print(1)
    elif (r_1 + r_2) ** 2 < distance or (r_1 - r_2) ** 2 > distance:
        print(0)
    else:
        print(2)