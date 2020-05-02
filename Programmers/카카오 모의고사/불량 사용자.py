def solution(user_id, banned_id):
    banned = [] # 금지된 아이디 목록
    for i in range(len(banned_id)):
        for j in range(len(user_id)):
            if isCheck(banned_id[i], user_id[j]):
                
    return answer