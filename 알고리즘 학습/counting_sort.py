# counting sort
# O(n+k)
# n이 비교적 작을 때에만 가능하다.

# 내 방법
def counting_sort(lst):
    # 배열 크기 최소화를 위해 O(N)으로 최대값 찾기
    max_num = max(lst)
    # counting을 위한 체크 리스트
    counter = [0 for _ in range(max_num+1)]
    # counter를 채우기 위해 lst 순회하기
    for i in range(len(lst)):
        counter[lst[i]] += 1
    # 결과를 위한 빈 리스트 생성
    result = []
    # counter를 순회하며 lst 채우기
    for i in range(len(counter)):
        result.extend([i]*counter[i])
    
    return result
    
print(counting_sort([3,1,6,2,1,0,0,1,2,6]))

# 더 효율적인 방법
def counting_sort2(lst):
    # 배열 크기 최소화를 위해 O(N)으로 최대값 찾기
    max_num = max(lst)
    # counting을 위한 체크 리스트
    counter = [0 for _ in range(max_num+1)]
    # counter를 채우기 위해 lst 순회하기
    for i in range(len(lst)):
        counter[lst[i]] += 1
    # 위치 파악을 위해 합을 중첩해 나가기
    for i in range(1, len(counter)):
        counter[i] += counter[i-1]
    # 결과를 위한 리스트 생성
    result = [0 for _ in range(len(lst))]
    # 해당 위치에 요소를 넣으며 위치를 -1 하며 재조정해나가기 
    # 역순으로 할 때에 시작 값이 len(lst)로 착각하지 않게 조심한다.
    for i in range(len(lst)-1, -1, -1):
        # 예를 들어, 3이면 3번째 칸이므로 3-1 index에 넣어주어야 한다.
        result[counter[lst[i]]-1] = lst[i]
        counter[lst[i]] -= 1
    return result

print(counting_sort2([3,1,6,2,1,0,0,1,2,6]))