# 2747번

# 동적 계획법 사용

def fibo(n):
    cache = [0 for _ in range(n+1)]
    cache[1] = 1

    for i in range(2, n+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[n]

print(fibo(int(input())))


# 재귀 사용

# def fibo(n):
#     if n <= 1:
#         return n
#     return fibo(n-1) + fibo(n-2)