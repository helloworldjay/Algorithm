# 측정된 심박수를 기준으로 운동의 종류를 결정한다.
# 최대 심박수 = (220 - 나이)
# 나이가 정수로 주어짐
age = int(input())
max_heartbeat = 220 - age
# 운동 종류를 저장할 리스트
work_type = [0 for _ in range(6)]
# 입력이 끝날 때 까지 반복
while True:
    try:
        # 입력이 숫자로 들어오면 연산을 시작
        heartbeat = int(input())
    # 입력이 공백으로 들어오면 연산을 종료
    except EOFError:
        break
    ratio = (heartbeat/max_heartbeat)*100
    # 비율이 90프로 이상이면 최고강도
    if ratio >= 90:
        work_type[0] += 1
    # 비율이 80프로 이상이면 고강도
    elif ratio >= 80:
        work_type[1] += 1
    # 비율이 80프로 이상이면 중강도
    elif ratio >= 75:
        work_type[2] += 1
    # 비율이 80프로 이상이면 집중
    elif ratio >= 68:
        work_type[3] += 1
    # 비율이 80프로 이상이면 워밍업
    elif ratio >= 60:
        work_type[4] += 1
    # 비율이 60프로 미만이면 휴식
    else:
        work_type[5] += 1

for i in range(6):
    print(work_type[i], end =' ')


