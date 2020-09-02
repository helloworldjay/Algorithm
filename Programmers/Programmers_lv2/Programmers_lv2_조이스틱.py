# 움직여야되는 횟수 찾는 함수
def find_cnt(target):
    return 26 - (ord(target) - 65) if ord(target) - 65 > 13 else (ord(target) - 65)

def direction(lst, idx):
    right = 0
    left = 0
    # 움직여야 하는 방향을 출력해주는 함수
    # idx를 기준으로 lst를 양쪽으로 정확히 절반으로 바꿔야할 개수를 count해준다   
    for i in range(1, len(lst)-1):
        if lst[(i+idx)%len(lst)] != 0 :        
            right = i
            break
    for i in range(1, len(lst)-1):
        if lst[idx-i] != 0 :
            left = i
            break
    return left, right

def solution(name):
    # 전체 횟수
    total_cnt = 0
    # 처음에는 A로만 이루어져있다.
    target = "A" * len(name)
    # 아스키코드 65 ~ 90
    # 각 자리수별로 움직여야되는 횟수를 저장
    cnt = [0]*len(name)
    for i in range(len(name)):
        # cnt의 i번째 요소는 name의 i번째 요소를 만들기 위한 횟수
        cnt[i] = find_cnt(name[i])
    # 이동할 인덱스
    idx = 0
    while True:
        # idx 위치의 알파벳을 바꿔준다
        total_cnt += cnt[idx]
        # 변경되었으므로 cnt를 초기화
        cnt[idx] = 0
        # 모든 요소가 0이면 반환하고 함수 종료
        if sum(cnt) == 0:
            return total_cnt
        # idx에서 어느 방향으로 움직여야할지 결정해주는 함수
        left, right = direction(cnt,idx)
        if left > right:
            idx += right
            total_cnt += right
        else :
            idx -= left
            total_cnt += left
    return total_cnt
print(solution("BBBAAAB"))
# 0000000    9


def direction(lst, idx):
    right = 0
    left = 0
    # 움직여야 하는 방향을 출력해주는 함수
    # idx를 기준으로 lst를 양쪽으로 정확히 절반으로 바꿔야할 개수를 count해준다
    for i in range(idx+1, idx+(len(lst)//2)+1):
        if lst[i%len(lst)] != 0 :
            right += 1
    for i in range(idx-1, idx-1-(len(lst)//2),-1):
        if lst[i%len(lst)] != 0 :
            left += 1
    # 오른쪽으로 바꿔야될 수가 더 많으면 오른쪽으로 이동
    if right >= left :
        return True
    # 왼쪽으로 바꿔야될 수가 더 많으면 왼쪽으로 이동 
    else :
        return False