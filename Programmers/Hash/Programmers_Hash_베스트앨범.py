def playtimes(genres, plays):
    playtime ={}
    for i in range(len(genres)):
        if genres[i] not in playtime :
            playtime[genres[i]] = 0
        playtime[genres[i]] += plays[i]
    playtimes = list(playtime.items())
    return sorted(playtimes,key= lambda x : -x[1]) # 위에 붙이면 안나오네..

def solution(genres, plays):
    genrelist = playtimes(genres,plays)
    anslist = []
    app = anslist.append
    for i in range(len(genrelist)):
        top1 = 0
        top2 = 0
        top1idx = -1
        top2idx = -1
        for j in range(len(genres)):
            if genres[j] == genrelist[i][0]:
                if plays[j] > top1:
                    top2 = top1
                    top2idx = top1idx
                    top1 = plays[j]
                    top1idx = j
                elif plays[j] > top2:
                    top2 = plays[j]
                    top2idx = j
        app(top1idx)
        if top2idx != -1:
            app(top2idx)
    return anslist



print(solution(["classic","pop","classic","classic","pop"],[500,600,150,800,2500]))











# def solution(genres, plays):
#     awsdict = {}
#     for i in range(len(genres)):
#         if genres[i] not in awsdict.keys() : # 이미 key 안에 존재하는지 check
#             awsdict[genres[i]] = plays[i]
#         else :
#             awsdict[genres[i]] += plays[i] # 이미 존재하는 장르이면 기존 값에 추가
    
#     genrelist = sorted(awsdict.items(), key = lambda x : x[1], reverse = True) # 재생 순위로 정렬
#     answerlist = []
#     for j in range(len(genrelist)): # 많이 재생된 장르를 가진 index를 plays에서 검색
#         genreidx = []
#         for k in range(len(genres)):
#             if genres[k] == genrelist[j][0]: # 특정 장르를 가진 index의 재생 횟수를 저장한다
#                 genreidx.append(plays[k])
#         genreidx.sort(reverse=True) # 역순으로 정렬
#         if len(genreidx) > 1 :
#             answerlist.append(plays.index(genreidx[0])) # 특정 장르의 첫번째로 많이 재생된 목록의 idx 삽입
#             answerlist.append(plays.index(genreidx[1])) # 특정 장르의 두번째로 많이 재생된 목록의 idx 삽입
#         else :
#             answerlist.append(plays.index(genreidx[0])) # 특정 장르의 첫번째로 많이 재생된 목록의 idx 삽입        
            
#     return answerlist