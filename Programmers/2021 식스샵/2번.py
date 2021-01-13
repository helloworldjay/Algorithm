def solution(grade):
    result = [0 for _ in range(len(grade))]
    grade_check = []
    for index, score in enumerate(grade):
        grade_check.append((score, index))
    grade_check.sort(reverse=True)
    ranking = 0
    score = 1000000001
    for i in range(len(grade_check)):
        check_grade, check_index = grade_check[i]
        if score > check_grade:
            ranking = i + 1
            result[check_index] = ranking
            score = check_grade
        elif score == check_grade:
            result[check_index] = ranking
    return result

print(solution([3,2,1,2]))