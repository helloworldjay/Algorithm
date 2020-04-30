from sys import stdin
n = int(stdin.readline()) # 새의 수
k = 1 # 노래하는 자연수
sec = 0 # 시간
total = 0 # 노래하는 총 시간
while n >= total :
    if n-total >= k:
        sec += 1
        total += k
        k += 1
    elif n == total:
        break
    else :
        k = 1
        
print(sec)
