n = int(input())
for i in range(n):
    mintime, maxtime, curtime = map(int, input().split())
    if curtime < mintime :
        print("#{} {}".format(i+1, mintime - curtime))
        continue
    elif curtime > maxtime :
        print("#{} {}".format(i+1, -1))
        continue
    else :
        print("#{} {}".format(i+1, 0))
    