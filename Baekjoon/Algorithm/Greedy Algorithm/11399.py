from sys import stdin

waitnumber = int(stdin.readline()) # 대기자 수
timelist = list(map(int,stdin.readline().rstrip().split())) # 대기 시간 리스트
timelist.sort() #대기 시간 정렬
leasttime = 0
for i in range(waitnumber):
    leasttime += (waitnumber-i)*timelist[i]
print(leasttime)
