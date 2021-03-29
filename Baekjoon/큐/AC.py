from sys import stdin
from collections import deque
input = stdin.readline
testcase = int(input())
for _ in range(testcase):
    orders = input().strip().replace("RR", "")
    orders = deque(list(orders))
    n = int(input())
    integer_list = deque(list(input().strip().lstrip('[').rstrip(']').split(',')))
    isCheck = True
    while orders:
        order = orders.popleft()
        if order == "R":
            integer_list.reverse()
            continue
        else:
            if integer_list:
                integer_list.popleft()
            else:
                isCheck = False
                break
    print("["+",".join(integer_list)+"]") if isCheck and integer_list else print("error")