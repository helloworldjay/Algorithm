# 1시간 20분
from itertools import combinations
# 최소성을 체크

def minimum_check(test, result):
    #case는 result의 요소중 하나인 튜플
    for case in result:
        for i in range(len(case)):
            if case[i] in test:
                if i == len(case)-1:
                    return False
            else:
                break
    return True
            
def unique_check(lst):
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                return False
    return True        

def solution(relation):
    # 결과를 담을 리스트
    result = []
    column_num = len(relation[0])
    columns = [i for i in range(column_num)]
    combi_columns = []
    for i in range(column_num):
        combi_columns.extend(list(combinations(columns,i+1)))
    for i in range(len(combi_columns)):
        # test할 칼럼의 종류
        test = combi_columns[i]
        sliced_relation = []
        for idx in range(len(relation)):
            # relation에서 row를 하나씩 불러오며 원하는 인덱스 요소만 잘라온다.
            temp = []
            for j in range(len(relation[0])):
                # test할 칼럼의 요소면 담는다.
                if j in test:
                    temp.append(relation[idx][j])
            sliced_relation.append(temp)
        # 중복이 존재하지 않는다면 유일성 만족
        if unique_check(sliced_relation):
            # 최소성을 체크
            if minimum_check(test, result):
                result.append(test)
    return len(result)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])) 
