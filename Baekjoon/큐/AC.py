from sys import stdin
from collections import deque
input = stdin.readline
T = int(input())
result = []
for _ in range(T):
    reversed = False
    function = input().strip()
    n = int(input())
    array = deque(list(input().lstrip('[').rstrip(']\n').split(',')))
    if len(array) < function.count('D') or array[0] == '':
        result.append("error")
        continue
    function = function.replace("RR", "")
    for one_function in function:
        if one_function == "R":
            reversed = False if reversed else True
        elif one_function == "D":
            if reversed:
                array.pop()
            else:
                array.popleft()
    if reversed:
        array.reverse()
    result.append(f"[{','.join(array)}]")
print('\n'.join(result))



# from sys import stdin
# from collections import deque
# input = stdin.readline
# testcase = int(input())
# for _ in range(testcase):
#     orders = input().strip().replace("RR", "")
#     orders = deque(list(orders))
#     n = int(input())
#     integer_list = deque(list(input().strip().lstrip('[').rstrip(']').split(',')))
#     isCheck = True
#     while orders:
#         order = orders.popleft()
#         if order == "R":
#             integer_list.reverse()
#             continue
#         else:
#             if integer_list:
#                 integer_list.popleft()
#             else:
#                 isCheck = False
#                 break
#     print("["+",".join(integer_list)+"]") if isCheck and integer_list else print("error")