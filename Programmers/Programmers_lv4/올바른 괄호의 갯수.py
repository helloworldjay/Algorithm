def factorial(n:int) -> int:
    if n == 1:
        return 1
    return n*factorial(n-1)
def solution(n: int) -> int:
    return factorial(2*n)//((n+1)*(factorial(n)**2))

print(solution(4))
