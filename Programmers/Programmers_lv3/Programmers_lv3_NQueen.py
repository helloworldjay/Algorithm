def check(x, row):
    # x 이전까지 행을 검사한다.
    for i in range(x):
        # 이미 해당 열이 차지되어 있다면
        if row[i] == row[x] or (abs(row[x] - row[i]) == x - i):
            return False
    return True


def dfs(r, row):
    global result
    # 마지막까지 도달 가능하면 개수를 1 증가
    if r == len(row):
        result += 1
    # 아직 도달하지 않았다면
    else:
        # 모든 인덱스를 검사
        for i in range(len(row)):
            # r번째 행에서 i번째 열에 퀸을 놓았다고 가정한다.
            row[r] = i
            # 위에서 i번째 열에 놓는 것으로 갱신을 해주었기 때문에 아래에서 가능한지 체크
            # 만약 r행 i열에 놓는 것이 가능하다면
            if check(r, row):
                # 다음 행도 검사한다.
                dfs(r+1,row)


def solution(n):
    global result
    # 각 행에서 놓여진 queen의 col 값을 요소로 같는 리스트
    row = [False] * n
    # 가능한 경우의 수를 담을 변수
    result = 0
    # dfs는 행을 입력받아 검색을 하는 함수
    dfs(0, row)

    return result

print(solution(10))