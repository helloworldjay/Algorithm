# 30분
def solution(msg):
    # 사전 만들기
    dictionary = {}
    idx = 1
    for i in range(65,91):
        dictionary[chr(i)] = idx
        idx += 1
    # 결과를 넣을 리스트
    result = []
    # 사전에 존재하는 부분까지 저장하기 위한 임시저장문자열
    temp = ""
    start = 0
    end = 0
    while True:
        temp = msg[start:end+1]
        value = dictionary.get(temp, -1)
        # 만약 사전에 존재하면 다음으로 이동
        if value != -1:
            end += 1
            if len(msg) == end:
                result.append(value)
                break
        # 사전에 존재하지 않을 때
        else :
            # 결과에 가능한 부분의 값 넣기
            result.append(dictionary.get(msg[start:end]))
            dictionary[temp] = idx
            idx += 1
            temp = []
            start = end 
    return result

print(solution("KAKAO"))

