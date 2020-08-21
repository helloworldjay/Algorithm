# binary search (이진 탐색)
# 주어진 리스트를 절반씩 줄여가며 탐색
# O(logN)의 속도
# 이미 정렬되어 있는 리스트에서만 사용 가능

# iteration 사용

def b_search_e(lst, target):
    start_idx = 0
    end_idx = len(lst)-1
    # idx의 역전이 일어날 때까지 순회
    while start_idx <= end_idx :
        # 기준값 설정
        target_idx = (start_idx + end_idx)//2
        
        if lst[target_idx] > target:
            end_idx = target_idx - 1
        elif lst[target_idx] < target:
            start_idx = target_idx + 1
        else :
            return target_idx
    
    return -1


# recursive 사용

def b_search_r(lst, target, start_idx, end_idx):
    # 기저조건 생성
    if start_idx > end_idx :
        return -1
    # 기준 index 생성
    target_idx = (start_idx + end_idx) // 2
    # 재귀를 할 때 return을 해주어야 한다. return으로 결과값을 도출하지 않으면 그냥 선언일 뿐이다.
    if lst[target_idx] > target:
        return b_search_r(lst, target,start_idx, target_idx - 1)
    elif lst[target_idx] < target:
        return b_search_r(lst, target, target_idx+1, end_idx)
    else:
        return target_idx  
    

n = int(input())
num_list = sorted(list(map(int, input().split())))

m = int(input())
for find_num in list(map(int, input().split())):
    if b_search_r(num_list, find_num, 0, len(num_list)-1) >= 0:
        print("1")
    else:
        print("0")