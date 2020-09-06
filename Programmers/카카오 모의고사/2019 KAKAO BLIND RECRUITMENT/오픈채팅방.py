# 21분
def solution(record):
    result = []
    # key : id, value : nickname
    id_nickname = {}
    for i in range(len(record)):
        temp_record = list(record[i].split())
        if temp_record[0] == "Enter":
            result.append((temp_record[1],"님이 들어왔습니다."))
            # id에 nickname 설정
            id_nickname[temp_record[1]] = temp_record[2]
        # 나가는 경우를 count하기 위해 닉네임에 변화를 주면 최종적인 답에 문제가 생긴다.
        elif temp_record[0] == "Leave":
            result.append((temp_record[1],"님이 나갔습니다."))
        else :
            id_nickname[temp_record[1]] = temp_record[2]
    for i in range(len(result)):
        result[i] = id_nickname[result[i][0]]+result[i][1]
    return result

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))