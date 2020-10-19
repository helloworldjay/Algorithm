# dp를 활용
from sys import stdin,setrecursionlimit
input = stdin.readline
code = input().strip()
if code[0] == "0" or not code[0].isdecimal(): 
    print("0")
    exit()
mod = 1000000
cache = [1, 1] # 0번 인덱스와 1번 인덱스 연산을 위해 1 ,1 로 초기화해준다. 
for i in range(1, len(code)):
    cnt = 0
    if int(code[i]) > 0 and code[i].isdecimal():
        cnt += cache[-1] # 지금 관찰하는 i인덱스의 바로 앞 값 i-1 인덱스까지 만들 수 있는 개수를 더해준다.
    if 10<= int(code[i-1:i+1])<27:
        cnt += cache[-2] # i-2번째까지의 암호 개수에 i-1,i 인덱스의 숫자를 2자리 숫자로 넣는 개념
    cache.append(cnt%mod)
print(cache[-1])
print(cache)

# dfs를 활용
# setrecursionlimit(100000)
# code = input().strip()
# cnt = 0
# def search(i):
#     global cnt 
#     if i >= len(code)-1: # code의 끝까지 갔다면
#         cnt = (cnt + 1)%1000000 # 개수를 한개 늘려준다.
#         return None
#     if code[i] == "0" or not code[i].isdecimal() : return None # 0이 숫자가 될 수 없으므로
#     if code[i:i+2].isdecimal() and 10 <= int(code[i:i+2]) <= 26: # 다음 자리수를 포함해서 2자리수가 가능하면
#         search(i+2) # 2자리 수를 경우에 포함하고 그 이후를 체크해본다.
#     search(i+1) # 한자리 수를 알파벳에 포함하고 그 다음을 체크한다.   
# search(0)
# print(cnt)




# from sys import stdin
# input = stdin.readline
# div = 1000000
# code = input().strip()
# cache = [1,0] # 0번 인덱스는 마지막 경우가 1자리인 경우의 수, 1번 인덱스는 마지막 경우가 2자리인 경우의 수
# for i in range(len(code)):
#     if code[i] == "0":
#         if i == 0 or int(code[i-1]) > 2: 
#             cache = [0,0]
#             break
#         else: 
#             cache = [0, cache[0]]
#     else: # i번째 요소가 0이 아닐 때
#         if i == 0 or code[i-1] !="0": # 앞에 숫자가 0이 아니거나 없다면
#             if int(code[i-1]+code[i]) <= 26:
#                 cache[0], cache[1] = (cache[0]+cache[1])%div, cache[0]
#             else :
#                 cache = [(cache[0]+cache[1])%div, 0]
#         elif i != 0 and code[i-1] == "0":
#             cache = [cache[1], 0]
# print((cache[0]+cache[1])%div)

        