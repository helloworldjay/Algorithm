def solution(numbers):
    num_str_list = list(map(str, numbers)) # numbers를 string으로 변환
    answer = sorted(num_str_list, key = lambda x : (x*4), reverse=True) # 반례 [0,0,0,0]
    return ''.join(answer) if answer[0] != "0" else "0" # 최대 4자리 까지 가능하므로 string을 연속해서 써 비교한다
    
print(solution([3,30,34,9,5]))

