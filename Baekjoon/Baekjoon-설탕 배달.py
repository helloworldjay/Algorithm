# 2839번
from sys import stdin
def minnum(total) :
    n = 0 # 개수
    if (total % 5) % 3 == 0 :
        n += (total//5) + ((total%5)//3)
        return n
    elif (total % 3) == 0 :
        n += total//3
        return n
    else : 
        return -1

tt = int(stdin.readline())
print(minnum(tt))
