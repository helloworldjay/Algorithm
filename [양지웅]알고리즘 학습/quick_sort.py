# pivot을 기준으로 그룹을 나눠 정렬하는 방식
# pivot 선택 방식에 따라 속도가 크게 차이난다.
# 최악의 경우 n^2의 속도가 날 수 있으므로 pivot을 잘 선택해야 한다. 
# 정렬이 되지 않은 리스트의 경우 중앙값이 가운데 값이 아니므로 시작값, 중간값, 마지막 값 중 가운데 값을 피봇으로 설정한다.

def quick_sort(lst):
    # 기저조건 만들기
    if len(lst) <= 1:
        return lst

    # 효율적인 피봇 만들기
    pivot_list = [
        lst[0],
        lst[(len(lst)-1)//2],
        lst[len(lst)-1]
    ]
    # 선형시간이 걸려 pivot list 3개 인자 중 가운데 것을 찾는다.
    pivot = sum(pivot_list) - max(pivot_list) - min(pivot_list)

    # pivot 기준으로 담을 배열을 결정
    left = []
    middle = []
    right = []

    # pivot 기준으로 담기
    for n in lst:
        # 여기서 비교 대상이 lst[pivot]이 아닌 pivot이다. pivot 자체가 비교 대상이다.
        if n > pivot:
            right.append(n)
        elif n < pivot:
            left.append(n)
        else :
            middle.append(n)
    # merge는 그냥 붙여주기만 해도 된다.
    return quick_sort(left) + middle + quick_sort(right)


l = [1,4,2,7,5,4,2]

print(quick_sort(l))