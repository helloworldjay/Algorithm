
# 리스트 내포 가능을 이용해 피보나치 수열 10번째까지 출력하는 프로그램을 작성하십시오.


cache = [0 for i in range(11)]
cache[1] = 1
def fibo(n):
    if n <= 1:
        return n
    if cache[n]:
        return cache[n]
    cache[n] = fibo(n-1) + fibo(n-2)
    return cache[n]
fibo(10)
print(cache[1:])