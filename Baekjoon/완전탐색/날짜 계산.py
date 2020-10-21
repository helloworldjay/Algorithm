from sys import stdin
input = stdin.readline
E, S, M = map(int, input().split()) # 15 28 19
if E == 15 : E = 0
if S == 28 : S = 0
if M == 19 : M = 0
year = 1
while year%15 != E or year%28 != S or year%19!=M :
    year += 1
print(year)