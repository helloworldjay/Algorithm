# 55분
# 날짜를 넣으면 시작시간과 종료 시간을 반환하는 함수
# 날짜는 고정되어 있으므로 시간, 분, 초만 생각하면 된다.
def time_log(line):
    # 2016년 9월 15일은 고정, 종료 시간, 프로세스 시간
    yymmdd, hhmmss, process = line.split()
    hh,mm,ss = hhmmss.split(':')
    hh,mm,ss = int(hh), int(mm), float(ss)
    # 소수점 연산의 경우 이진분수 표현 문제로 오류가 발생하므로 1000을 곱해 소수점 처리를 해준다.
    process= int(float(process[:-1])*1000)
    end_time = int((hh*3600 + mm*60 + ss)*1000)
    start_time = end_time - process + 1
    return start_time, end_time
    
def solution(lines):
    for idx in range(len(lines)):
        lines[idx] = time_log(lines[idx])
    # lines를 시작 시점을 기준으로 정렬
    lines.sort()
    max_cnt = 0
    for i in range(len(lines)):
        cnt = 0
        # 새로 시작하는 요소 앞의 1초를 탐색한다.
        target_time = lines[i][0]-1000
        for j in range(i+1):
            if lines[j][1] > target_time:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    return max_cnt

print(solution(	["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))

