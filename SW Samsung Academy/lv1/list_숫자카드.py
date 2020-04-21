
t = int(input())
for i in range(t):
    n = int(input()) # 카드 수
    nlist = list(map(int, input())) # 카드 종류
    nset = sorted(list(set(nlist))) # 중복 제거
    cnt = 0 # 최대 카드 수
    card = 0 # 최대개수 카드 번호
    for j in range(len(nset)):    
        if nlist.count(nset[j]) >= cnt :
            card = nset[j]
            cnt = nlist.count(nset[j])
    print("#{} {} {}".format(i+1, card, cnt))

