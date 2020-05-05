arry = []
n = int(input())
for _ in range(n):
    arry.append(int(input()))
arry.sort()
#평균
mean = int(round(sum(arry)/n,0))
#중앙값
median = arry[n//2]
#최빈값
cnt = 0
mx = []
temp = list(set(arry))
for i in range(len(temp)):
    cnt = arry.count(temp[i]) if arry.count(temp[i]) > cnt else cnt
for i in range(len(temp)):
    if arry.count(temp[i]) == cnt:
        mx.append(temp[i])
mx.sort()
if len(mx) >= 2:
    mf = mx[1]
else :
    mf = mx[0]        
# 범위
rnge = arry[-1] - arry[0]
print(mean, median, mf, rnge, sep= "\n")