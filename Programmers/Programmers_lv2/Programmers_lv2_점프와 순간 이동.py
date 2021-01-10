def solution(n: int) -> int:
    fuel = 1
    while n > 1:
        if n % 2 == 1:
            fuel += 1
            n -= 1
            continue
        n //= 2
    return fuel


print(solution(5000))
