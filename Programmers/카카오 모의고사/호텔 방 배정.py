def solution(k, room_number):
    room = [1 for _ in range(k+1)] # idx가 방 번호, 1은 방을 쓸 수 있다는 뜻
    dp = [i for i in range(k+1)] # 부모 노드
    room[0] = 0
    result = []
    for pre in room_number: # 선호하는 방 번호를 하나씩 꺼내옴
        if room[pre] == 1 :
            room[pre] = 0
            dp[pre] += 1 
            result.append(pre)
        else:
            while True:
                if room[dp[pre]] == 1:
                    room[pre] = 0
                    dp[pre] += 1 
                    result.append(pre)
                    
    return result
print(solution(10, [1,3,4,1,3,1]))