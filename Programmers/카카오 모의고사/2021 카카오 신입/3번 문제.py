def solution(info, query):
    #info의 정보들을 튜플로 바꿔준다.
    for i in range(len(info)):
        info[i] = tuple(info[i].split())
    # 정답을 담을 리스트
    result = [0 for _ in range(len(query))]
    info.sort()
    index_info = {}
    language = ["cpp","java","python"]
    field = ["backend", "front_end"]
    level = ["junior", "senior"]
    food = ["chicken","pizza"]
    for i in range(3):
        index_info[language[i]] = {}
        for j in range(2):
            index_info[language[i]][field[j]] = {}
            for k in range(2):
                index_info[language[i]][field[j]][level[k]] = {}
                for l in range(2):
                    index_info[language[i]][field[j]][level[k]][food[l]] = []
    start = 0
    for i in range(len(query)):
        # query[i] 의미하는 바는 검색해야할 조건이다. 검색할 조건을 리스트로 분리
        query[i] = list(query[i].split(" and "))
        food, score = query[i][-1].split()
        query[i] = query[i][:-1] + [food, score]
        print(query[i])
        
        
    return index_info


# 30분
# 정확성만 통과
# def solution(info, query):
#     #info의 정보들을 튜플로 바꿔준다.
#     for i in range(len(info)):
#         info[i] = tuple(info[i].split())
#     # 정답을 담을 리스트
#     result = [0 for _ in range(len(query))]
#     # 검색할 쿼리를 결정
#     for i in range(len(query)):
#         # info의 개수
#         cnt = 0
#         # query[i] 의미하는 바는 검색해야할 조건이다. 검색할 조건을 리스트로 분리
#         query[i] = list(query[i].split(" and "))
#         food, score = query[i][-1].split()
#         query[i] = query[i][:-1] + [food, score]
#         for idx in range(len(info)):
#             if (info[idx][0] == query[i][0] or query[i][0] == '-') and (info[idx][1] == query[i][1] or query[i][1] == '-') and (info[idx][2] == query[i][2] or query[i][2] == '-') and (info[idx][3] == query[i][3] or query[i][3] == '-') and int(info[idx][4]) >= int(query[i][4]):
#                 cnt +=1
#         result[i] = cnt
        
#     return result

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))