# 30분
from itertools import combinations
def order_combi(order, number):
    # order를 넣었을 때 number씩 묶어서 반환해준다. 
    # "ABCFG"를 넣으면 number가 2개라면 "AB", "AC"
    order_list = list(combinations(list(order), number))
    for i in range(len(order_list)):
        order_list[i] = ''.join(order_list[i])
    return order_list

# temp를 집어 넣었을 때 가장 인기 많은 메뉴 조합을 추천해주는 함수
def recommend(temp_list):
    menu = {}
    for i in range(len(temp_list)):
        for j in range(len(temp_list[i])):
            menu[temp_list[i][j]] = menu.get(temp_list[i][j],0) + 1
    max_val = -1
    if len(menu) != 0: 
        max_val = max(menu.values())
    best = []
    if max_val>=2:
        for key, value in menu.items():
            if value == max_val:
                best.append(key)
    return best

def solution(orders, course):
    # orders를 정렬해준다.
    for i in range(len(orders)):
        orders[i] = ''.join(sorted(list(orders[i])))
    result = []
    # course의 경우를 하나씩 본다.
    for i in range(len(course)):
        temp = []
        # course[i]는 2,3,4
        for j in range(len(orders)):
            temp.append(order_combi(orders[j],course[i]))
        result.extend(recommend(temp))
    return sorted(result)

print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))