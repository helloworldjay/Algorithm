# 1065번
from sys import stdin
def hansu(n): # 한 수 판별
    nlist = list(map(int, list(str(n))))
    try :
        d = nlist[1] - nlist[0]
    except :
        return True
    for i in range(len(nlist)-1):
        if d != nlist[i+1] - nlist[i]:
            return False
    return True

num = int(stdin.readline())
han = 0
for i in range(1,num+1):
    if hansu(i) == True :
        han += 1
print(han)