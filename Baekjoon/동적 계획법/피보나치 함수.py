t = int(input()) # testcase num
tc = [] # testcase 
for _ in range(t):
    tc.append(int(input()))
def fibo(n):        
    cache = [[0, 0] for _ in range(n+1)]
    if n == 0 :
        return [1, 0]
    cache[0] = [1, 0]
    cache[1] = [0, 1]
    for i in range(2, n+1):
        cache[i] = [cache[i-1][0] + cache[i-2][0],cache[i-1][1] + cache[i-2][1]] 
    return cache[n]
for i in range(t):
    tmp = fibo(tc[i])
    print(tmp[0], tmp[1])

