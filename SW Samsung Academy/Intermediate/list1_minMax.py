import math
# testcase 수
T = int(input())
# 결과를 담을 리스트
# 선형으로 조회하면 O(N)이 된다.
result = []
for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    min_val = math.inf
    max_val = -math.inf
    for i in range(N):
        if min_val > a[i]: 
            min_val = a[i]
        if max_val < a[i]:
            max_val = a[i]
    result.append(max_val-min_val)

# 자료를 출력
for i in range(T):
    print(f"#{i+1} {result[i]}")


# 예전 풀이
# sorted를 사용했으므로 O(NlogN)이 된다.

num_TestCase = int(input()) # TestCase의 개수
for i in range(num_TestCase):
    num_elements = int(input()) # 양수의 개수
    lst = list(map(int, input().split())) # 개수 만큼 양수 받기
    print("#{} {}".format(i+1, sorted(lst)[len(lst)-1]-sorted(lst)[0]))
