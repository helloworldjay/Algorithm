from sys import stdin

input = stdin.readline
left, right = list(input().strip()), []
n = int(input().strip())
for _ in range(n):
    order = input().strip()
    if order == "L" and left:
        right.append(left.pop())
    elif order == "D" and right:
        left.append(right.pop())
    elif order == "B" and left:
        left.pop()
    elif order[0] == "P":
        left.append(order[2])
print(''.join(left + right[::-1]))
