from sys import stdin
st = stdin.readline().strip() # 문서 입력
t = stdin.readline().strip() # 검색할 목록

cnt = 0 # 몇번 나오는지 검색
i = 0 # index
while len(st)-i >= len(t):
    if st[i:i+len(t)] == t:   
        i += len(t)
        cnt += 1
    else :
        i += 1


print(cnt)        


# 거의 비슷한데 if 문의 개수와 구조에 따라 속도가 완전히 다름
# 아래 코드는 속도 이슈로 통과 x


# from sys import stdin
# def findstr(st, t): # string에서 target이 몇번 중복없이 존재하나 검색
#     cnt = 0 # 몇번 나오는지 검색
#     i = 0 # index
#     while len(st)-i >= len(t):
#         if st[i] != t[0]:
#             i += 1
#         else :
#             if st[i:i+len(t)] == t:   
#                 i += len(t)
#                 cnt += 1
#     return cnt

        

# doc = stdin.readline().strip() # 문서 입력
# tt = stdin.readline().strip() # 검색할 목록
# print(findstr(doc, tt))