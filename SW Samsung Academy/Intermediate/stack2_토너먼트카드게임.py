
# 가위바위보 조건 만들기
def win(lst, left_idx, right_idx):
    # win이라는 함수는 관찰하는 값이 인덱스이므로 인덱스만을 반환하게 한다.
    # 조건은 리스트의 해당 인덱스의 값으로 비교한다.
    if lst[left_idx] == 1:
        if lst[right_idx] == 1 or lst[right_idx] == 3:
            return left_idx
        else :
            return right_idx
    elif lst[left_idx] == 2:
        if lst[right_idx] == 3:
            return right_idx
        else :
            return left_idx
    else :
        if lst[right_idx] == 1 :
            return right_idx
        else :
            return left_idx

# 카드게임 
def cardgame(lst, start, end):
    # 기저조건
    # lst는 조건에서 변하지 않으므로 len(lst)==1 조건 사용 불가
    # 인덱스만 움직이므로 인덱스가 같아질 때, 즉 한 요소만 남았을 때 인덱스를 반환한다.
    if start == end:
        return start
    l_idx = cardgame(lst, start, (start+end)//2)
    r_idx = cardgame(lst, (start+end)//2+1, end)
    # 이긴 쪽 인덱스를 출력한다.
    return win(lst, l_idx, r_idx)
    
    
    

# testcase
T = int(input())

for idx in range(T):
    # 인원 수 받기
    N = int(input())
    # 카드의 종류 입력받기
    N_list = list(map(int, input().split()))
    result = cardgame(N_list,0,N-1)
    print(f"#{idx+1} {result+1}")
    