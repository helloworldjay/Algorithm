def solution(grades, weights, threshold):
    dict = {"A+":10, "A0":9, "B+":8, "B0":7, "C+":6, "C0":5, "D+":4, "D0":3, "F":0} # grade별 점수 선언
    total_grade = 0 # 가중치 합산 점수
    for i in range(len(grades)): # 조건상 grades와 weights의 길이는 같다
        total_grade += dict[grades[i]]*weights[i] # i+1번째 과목 성적을 가중치 계산하여 총점수에 합산
    return total_grade - threshold