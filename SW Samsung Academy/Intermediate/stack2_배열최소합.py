# row를 파라미터로 받는 최소 합을 찾는 함수
def find_min(row):
    global partial_sum, min_sum
    # pruning을 위한 조건
    # 부분합이 이미 최소합보다 크게되면 더 내려갈 의미가 없다.
    if partial_sum > min_sum:
        return
    # 마지막 행에 도달하면 종료한다.
    # 아직 더하는 연산이 없으므로 조건은 N-1이 아니라 N이 되어야한다.
    if row == N:
        # 마지막에 도달했는데 부분합이 최소합보다 작다면 갱신해준다.
        if partial_sum < min_sum:
            min_sum = partial_sum
    # i는 col를 의미한다
    for i in range(N):
        # 아직 방문하지 않은 col이라면
        if not visited[i]:
            # 특정 row의 i번째 값으로 결정이 되있을 때에
            # 방문으로 갱신
            visited[i] = True
            partial_sum += arry[row][i]
            # i로 결정했을 때 그 아래를 계산한다.
            find_min(row+1)
            # find_min이 바닥까지 가거나 pruning 된 후에야 위에 것이 끝나므로
            # 다시 현재 row로 올라와야 한다.
            visited[i] = False
            partial_sum -= arry[row][i]
            
    

# 테스트케이스 입력
T = int(input())
for idx in range(T):
    # 배열의 길이
    N = int(input())
    arry = [list(map(int, input().split())) for _ in range(N)]
    # 방문한 배열의 col 번호를 저장하기 위한 배열
    visited = [False] * N
    # 부분합과 최소값을 저장할 변수
    # (N이 10보다 작고 10보다 작은 자연수가 주어지므로 최소값의 시작은 1000이면 충분)
    partial_sum, min_sum = 0, 1000 
    # 최소 값을 찾기위한 함수
    find_min(0)
    print(min_sum)