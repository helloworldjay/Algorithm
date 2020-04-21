def mul(num, time):
    if time == 0 :
        return 1
    else : 
        return num * mul(num,time-1)

for i in range(10):
    trial = int(input()) # 시도 횟수
    num, time = map(int, input().split())
    print("#{} {}".format(trial, mul(num, time)))