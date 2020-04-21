#1. join 함수 2. swapcase
def solution(s):
    
    return ''.join(sorted(list(s), reverse = True))
print(solution("aekdiaBdeC"))