# 10039번
from sys import stdin
sum = 0
for _ in range(5):
    score = int(stdin.readline())
    sum += score if score >= 40 else (score + 40)
print(round(sum/5))

