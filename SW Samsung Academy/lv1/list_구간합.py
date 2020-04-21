t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    maxnum = 0
    minnum = 1000000
    nlist = list(map(int, input().split()))
    for j in range(n-m+1):
        total = sum(nlist[j:j+m])
        if total > maxnum :
            maxnum = total
        if total < minnum :
            minnum = total
    print("#{} {}".format(i, maxnum-minnum))