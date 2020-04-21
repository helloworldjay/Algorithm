# 4673번
from sys import stdin
def d(n):
    nlist = list(map(int, list(str(n)))) # 각 자리수 리스트
    return n + sum(nlist)
selfnum = [i for i in range(1, 10001)]
for i in range(1,10001):
    try :
        selfnum.remove(d(i))
    except :
        continue
for i in range(len(selfnum)):
    print(selfnum[i])