from sys import stdin
input = stdin.readline
def solution(target:int)->int:
    n = 0
    while True:
        if target <= 1+(3*n*(n+1)):
            return n + 1
        n += 1
print(solution(int(input())))