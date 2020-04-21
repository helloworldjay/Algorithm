def solution(num):
    cnt = 0
    while True :
        if num != 1 :
            num = num/2 if num%2 == 0 else num*3 + 1
            cnt += 1
            if cnt > 500 :
                return -1
        else:
            return cnt

print(solution(626331))