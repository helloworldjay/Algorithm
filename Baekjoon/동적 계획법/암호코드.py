from sys import stdin
input = stdin.readline
div = 1000000
code = input().strip()
cache = [1,0] # 0번 인덱스는 마지막 경우가 1자리인 경우의 수, 1번 인덱스는 마지막 경우가 2자리인 경우의 수
for i in range(len(code)):
    if code[i] == "0":
        if i == 0 or int(code[i-1]) > 2: 
            cache = [0,0]
            break
        else: 
            cache = [0, cache[0]]
    else: # i번째 요소가 0이 아닐 때
        if i == 0 or code[i-1] !="0": # 앞에 숫자가 0이 아니거나 없다면
            if int(code[i-1]+code[i]) <= 26:
                cache[0], cache[1] = (cache[0]+cache[1])%div, cache[0]
            else :
                cache = [(cache[0]+cache[1])%div, 0]
        elif i != 0 and code[i-1] == "0":
            cache = [cache[1], 0]
print((cache[0]+cache[1])%div)

        