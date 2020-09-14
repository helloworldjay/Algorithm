def solution(play_time, adv_time, logs):
    # playtime을 초로 변환
    hh, mm, ss = play_time.split(":")
    play_time = int(hh)*3600 + int(mm)*60 + int(ss)
    # adv_time을 초로 변환
    hh, mm, ss = adv_time.split(":")
    adv_time = int(hh)*3600 + int(mm)*60 + int(ss)
    # logs의 시작시간과 끝시간을 초로 바꿔 튜플로 넣어준다.
    for i in range(len(logs)):
        start, end = logs[i].split("-")
        hh,mm,ss = start.split(":")
        start = int(hh)*3600 + int(mm)*60 + int(ss)
        hh,mm,ss = end.split(":")
        end = int(hh)*3600 + int(mm)*60 + int(ss)
        logs[i] = (start,end)
    # logs들을 start시간 기준으로 정렬한다.
    logs.sort()
    # 가장 큰 수
    max_val = 0
    # 가장 빠른 시작 시간
    max_start = 0
    for i in range(len(logs)):
        # logs[i] 시작에 맞춰 광고를 틀 때 광고시간
        val = 0
        # 광고의 시작 시간, 광고 종료시간
        adv_start, adv_end = logs[i][0], logs[i][0] + adv_time
        # 만약 광고시간이 영상 종료보다 뒤면 틀수 없다.
        if adv_end > play_time:
            break
        idx =0
        while idx < len(logs):
            # start는 영상 재생의 시작, end는 영상 종료 시간
            start, end = logs[idx]
            # 영상 재생 시작시간이 광고 종료시간 이후면 종료한다.
            if start >= adv_end:
                break
            # 영상의 종료 시간이 광고 시작보다 앞이면 다음 것으로 넘어간다.
            if end < adv_start:
                idx += 1
                continue
            # start가 adv_start 이전이면
            if start < adv_start:
                # adv_end 가 end보다 이후면 val에 end-adv_start를 더해준다.
                if adv_end >= end:
                    val += (end-adv_start)
                # adv_end 가 end보다 빠르면 val에 adv_end - adv_start를 더해준다.
                else:
                    val += (adv_end-adv_start)
            # start가 adv_start보다 이후이면
            else:
                # adv_end가 end보다 이후면 val에 end-start를 더해준다.
                if adv_end >= end:
                    val += (end-start)
                # adv_end가 end보다 이전이면 val에 adv_end - start를 더해준다.
                else:
                    val += (adv_end-start)           
            idx += 1
        if val > max_val: 
            max_val = val
            max_start = adv_start
    mm, ss = divmod(max_start,60)
    hh, mm = divmod(mm,60)
    return f"{hh:#02d}:{mm:#02d}:{ss:#02d}"

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))