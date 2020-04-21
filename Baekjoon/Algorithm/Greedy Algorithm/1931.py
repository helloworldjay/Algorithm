from sys import stdin

num_meeting = int(stdin.readline().rstrip())
meetinglst = [] # 미팅 시간 리스트
for i in range(num_meeting):
    starttime, endtime = map(int, stdin.readline().rstrip().split()) # 미팅 시작 시간, 종료 시간 입력
    meetinglst.append((starttime, endtime))
meetinglst.sort() # 정렬
max_num = 0 # 최대 미팅 개수

