from sys import stdin
input = stdin.readline

N = int(input())
check = 666
while True:
    if '666' in str(check):
        N -= 1
        if N == 0: break
    check += 1
print(check)
