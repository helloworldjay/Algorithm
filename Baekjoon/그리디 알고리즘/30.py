# 30의 배수는 3의 배수이며 10의 배수이어야 하므로 우선 0이 있는지 판별하여 없으면 -1, 있으면 판별을 시작한다. 
# 0을 한개 제외한 수들의 총 합이 3의 배수이면 3의 배수이므로 내림차순으로 정렬하면 최대값이 된다. 

n = list(map(int,list(input())))
result = -1
if 0 in n:
    temp = sorted(n, reverse=True)
    temp.pop()
    if sum(temp) % 3 == 0:
        n = list(map(str, sorted(n, reverse=True)))
        result = ''.join(n)
print(result) 