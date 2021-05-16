def solution(numbers):
    result = []
    for number in numbers:
        temp = number
        while True:
            temp += 1
            if 1 <= bin(temp ^ number).count('1') < 3:
                result.append(temp)
                break
    return result

print(solution([2, 7]))
