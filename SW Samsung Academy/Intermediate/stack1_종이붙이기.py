def paper(n):
    nlist = [0,1,3]
    for i in range(3, n//10+1):
        nlist.append(nlist[i-1] + nlist[i-2]*2)
    return nlist[n//10]
    
n = int(input())
anslist = []
for i in range(n):
    anslist.append(int(input()))
for j in range(len(anslist)):
    print("#{} {}".format(j+1,paper(anslist[j])))
