from collections import deque
def solution(n, t, m, timetable):
    for i in range(len(timetable)):
        hh, mm = timetable[i].split(":")
        timetable[i] = int(hh)*60 + int(mm)
    timetable.sort()
    timetable = deque(timetable)
    # 버스 시작시간
    start_bus = 540
    # 막차시간
    last_bus = start_bus + t*(n-1)
    # 체크할 m을 저장
    check = m
    # 마지막 버스이후에 온 사람이 대기열 제일 첫번째면 그냥 막차시간에 타면 된다.
    if timetable[0] > last_bus:
        hh, mm = divmod(last_bus,60)
        return f"{hh:#02d}:{mm:#02d}"
    else:
        while True:
            if n != 1:
                # 만약 버스 시간보다 대기 시간이 더 빠르다면 대기열에서 제거해준다.
                if timetable[0] <= start_bus and check > 0:
                    timetable.popleft()
                    # 한명이 탔다
                    check -= 1
                # 버스에 탈 사람이 없거나 버스에 좌석이 없다면 
                else :
                    # 다음 버스로 이동
                    start_bus += t
                    # 남은 버스의 수를 하나 줄인다.
                    n -= 1
                    # 다시 좌석수를 리셋
                    check = m
            # 막차가 되었을 때
            else:
                # 아직 대기하는 사람이 있으면
                if len(timetable) != 0 :
                    # 좌석이 한자리 남은게 아니면
                    if check != 1:
                        # 대기하는 사람을 태운다.
                        timetable.popleft()
                        check -= 1
                    # 좌석이 한자리 남았으면
                    else:
                        # 처음사람보다 1분은 먼저 와야한다.
                        hh, mm = divmod(timetable[0]-1,60)
                        return f"{hh:#02d}:{mm:#02d}"
                # 이제 대기하는 사람이 없으면
                else :
                    hh, mm = divmod(start_bus,60)
                    return f"{hh:#02d}:{mm:#02d}"           
    

print(solution(	2, 10, 2, ["09:10", "09:09", "08:00"]))