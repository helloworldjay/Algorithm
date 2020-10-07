from sys import stdin
input = stdin.readline
A, P = input().split()
D = [A]
while True:
    A = D[-1]
    total = 0
    for i in range(len(A)):
        total += (int(A[i])**int(P)) # 각자리를 P제곱하여 더해준다
    if str(total) not in D:
        D.append(str(total))
    else : 
        print(D.index(str(total)))
        break