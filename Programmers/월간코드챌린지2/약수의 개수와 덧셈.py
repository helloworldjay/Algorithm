def solution(left, right):
    import math
    return sum([i for i in range(left, right+1) if math.sqrt(i) != int(math.sqrt(i))]) - sum([i for i in range(left, right+1) if math.sqrt(i) == int(math.sqrt(i))])