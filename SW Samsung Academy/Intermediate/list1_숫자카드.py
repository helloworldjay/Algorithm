T = int(input())
result = []

# 새로운 코드
# for문 안에서 추가적인 N 이상의 연산이 없으므로 O(N)의 속도가 된다.
for _ in range(T):
    counter = [0] * 10
    N = int(input())
    card_list = list(map(int, list(input())))
    mx = -1
    mxidx = -1
    for i in range(N):
        # 카운터의 개수 늘리기
        counter[card_list[i]] += 1
        # 카드 개수가 최대값으로 같을 경우 더 큰 숫자를 뽑기 위해 저장
        if counter[card_list[i]] == mx and card_list[i] > mxidx:
            mxidx = card_list[i]
        # 갱신된 카드 수가 더 크면 mx 갱신
        if counter[card_list[i]] > mx:
            mx = counter[card_list[i]]
            mxidx = card_list[i]
    result.append((mxidx, mx))

for i in range(T):
    print(f"#{i+1} {result[i][0]} {result[i][1]}")



# 예전 코드

# for문 안에 또 count를 사용하여 O(n^2)의 시간이 걸린다.
# 속도를 고려하지 않고 편하게 작성한 코드

# for i in range(t):
#     n = int(input()) # 카드 수
#     nlist = list(map(int, input())) # 카드 종류
#     nset = sorted(list(set(nlist))) # 중복 제거
#     cnt = 0 # 최대 카드 수
#     card = 0 # 최대개수 카드 번호
#     for j in range(len(nset)):    
#         if nlist.count(nset[j]) >= cnt :
#             card = nset[j]
#             cnt = nlist.count(nset[j])
#     print("#{} {} {}".format(i+1, card, cnt))

