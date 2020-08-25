# 부분 집합의 집합을 찾는 함수
def subset(lst):
    n = len(lst)
    # 부분 집합들을 담을 집합
    result = []
    # 2^n 까지 순회 (0, 1, 10, 11, ... ) 
    # -> (공집합, 마지막 요소만 포함, 마지막에서 2번째 요소만 포함, ...)
    for i in range(1<<n):
        # 새로운 i에서 부분집합을 초기화
        temp = []
        # 전체집합 lst의 원소를 첫번째부터 마지막까지 본다
        for j in range(n):
            # 1<<3 = 8
            # 예를 들어, i가 11로 고정되어 있으면 1<<j는 1을 0, 1, 2, .. 로 증가시키면서
            # i가 1인 부분에서만 요소를 추가한다. 이 때 j는 lst의 j번째 요소를 의미한다.
            if i&(1<<j):
                # i의 비트 자리가 1인 요소를 부분집합에 담는다.
                temp.append(lst[j])
        # 완성된 부분집합을 부분집합의 집합에 담아준다.
        result.append(temp)
    return result

A = [i for i in range(1,13)]
T = int(input())
subset_A = subset(A)
for idx in range(T):
    N, K = map(int, input().split())
    num_Subset = 0
    for i in range(len(subset_A)):
        # 부분집합의 개수가 N이면서 합이 K인 값의 개수를 더해준다.
        if sum(subset_A[i]) == K and len(subset_A[i]) == N:
            num_Subset += 1
    print(f"#{idx+1} {num_Subset}")

