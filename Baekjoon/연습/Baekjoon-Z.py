from sys import stdin
n, r, c = map(int, stdin.readline().split())
if r % 2 == 0:
    ex = 0 if c % 2 == 0 else 1
else :
    ex = 2 if c % 2 == 0 else 3 
ntime = (r//2)*(2**(n+1)) + 4*(c//2) + ex
print(ntime)