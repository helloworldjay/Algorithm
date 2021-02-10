n, k = map(int, input().split())
answer = []
index = 0
circle = [i for i in range(1, n + 1)]
for _ in range(n):
    index = (index + k - 1) % len(circle)
    answer.append(str(circle.pop(index)))
print("<" + ', '.join(answer) + ">")
