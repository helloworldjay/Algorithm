from sys import stdin
input = stdin.readline
N = int(input())
counts = 1
base = [0, 1] # 0번 인덱스 = 0의 개수, 1번 인덱스 = 1의 개수
while True:
    if counts == N: break
    counts += 1
    temp = [0,0]
    temp[0] = base[0] + base[1]
    temp[1] = base[0]
    base = temp
print(sum(base))