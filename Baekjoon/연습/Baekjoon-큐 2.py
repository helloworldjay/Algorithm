from sys import stdin
from collections import deque

n = int(stdin.readline()) 
ordlist = []
for _ in range(n):
    ordlist.append(stdin.readline().strip()) # n은 명령의 수, ordlist는 명령 리스트
queue = deque()
for order in ordlist:
    if order[:4] == "push": # 명령 시작이 push 라면
        queue.append(order[5:]) # 'push ' 이후 문자를 데크에 삽입
    elif order == "pop":
        print(queue.popleft()) if queue else print(-1)  # 가장 왼쪽 항목을 뺄 때 속도를 고려하기 위해 deque의 popleft 사용
    elif order == "size":
        print(len(queue)) # 길이 구하기
    elif order == "empty":
        print(0) if queue else print(1) # 비어있는지 여부
    elif order == "front":
        print(queue[0]) if queue else print(-1) # 가장 왼쪽값 구하기
    else :
        print(queue[-1]) if queue else print(-1) # 가장 오른쪽 값 구하기