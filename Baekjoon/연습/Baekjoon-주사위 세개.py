from sys import stdin
dice = list(map(int, stdin.readline().split()))
dice.sort()
if len(set(dice)) == 3 : # 중복 제거 결과물이 3개면
    print(100*max(dice))
elif len(set(dice)) == 2 : # 중복 제거 결과물이 2개면
    print(1000+100*(dice[1])) # 정렬하면 중복이 되는 수는 반드시 가운데 위치한다 (항이 3개이기 때문에)
else :
    print(10000 + 1000*(dice[0])) 
    