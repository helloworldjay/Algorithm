def solution(a, b):
    dow = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    days = [0,31,29,31,30,31,30,31,31,30,31,30]
    dates = b-1
    for i in range(a):
        dates += days[i]
    return dow[dates%7]

print(solution(2,1))