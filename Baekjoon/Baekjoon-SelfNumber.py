def selfnumber(n):
    sum = 0
    for i in map(int,list(str(n))):
        sum += i
    return n + sum 

lst = [i for i in range(1,10001)]

for i in range(1,10001):
    result = i
    while result <= 10000 :
        result = selfnumber(result)
        try:
            lst.remove(result)
        except:
            continue
for i in lst:
    print(i)
