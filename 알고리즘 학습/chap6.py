# 종만북(알고리즘 문제해결전략)
# 6.2 재귀 호출과 완전 탐색

 
 # 1부터 n까지의 합을 반환
# 조건 : n>=1
def newsum(n) :
    ret = 0
    for i in range(1, n):
        ret += i
    return ret


# 재귀를 사용
def recursiveSum(n):
    # 기저조건을 생성
    if n == 1 : return 1
    return n + recursive(n-1)


# n개의 원소 중 m개를 고르는 모든 조합을 찾는 알고리즘
# n : 전체 원소의 수
# picked : 지금까지 고른 원소들의 번호
# toPick : 더 고를 원소의 수

def pick(n, picked, toPick):
    # 기저 조건 : 더 고를 원소가 없을 때(이미 고를 개수를 다 고른 상황) 고른 원소들을 출력
    if toPick == 0 :
        print(picked)
        return
    # n개의 원소 중 선택된 것이 없다면 smallest에 0을 넣고, 선택된 것이 있다면 선택된 것 중 마지막 인덱스에 1을 더한다. 즉 채운 것 뒤부터 보겠다는 뜻
    smallest = 0 if not picked else len(picked)
    # 뽑아야 될 원소가 남은 상황에서 뽑힌 것 뒤부터 마지막 뽑을 것 까지 반복
    for next in range(smallest, n):
        # next가 돌아가면서 뽑히고 그 때 마다 picked에 저장된다.
        picked.append(next)
        # next가 뽑혀 picked에 저장되고 뽑을 개수가 하나 줄어든 상황
        pick(n, picked, toPick - 1)
        # 
        picked.pop()

pick(5, [], 3)
    