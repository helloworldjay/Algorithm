def solution(n, lost, reserve):
    students = [1 for i in range(n)]
    for j in range(len(lost)) :
        students[lost[j]-1] -= 1
    for k in range(len(reserve)):
        students[reserve[k]-1] += 1
    for i in range(len(students)):
        if students[i] == 0:
            if i-1 >= 0 and students[i-1] == 2 :
                students[i-1] -= 1
                students[i] = 1
            elif i+1 <= n-1 and students[i+1] == 2 : 
                students[i+1] -= 1
                students[i] = 1
    answer = students.count(1) + students.count(2)
    return answer
print(solution(5,[2,4],[1,3,5]))