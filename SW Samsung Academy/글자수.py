t = int(input()) # testcase
result = []
for _ in range(t):
    m = 0 # 최대값
    a , b = list(set(input())), input()
    for i in range(len(a)):
        temp = b.count(a[i])
        if temp > m :
            m = temp
    result.append(m)

for i in range(t):
    print("#{} {}".format(i+1, result[i]))