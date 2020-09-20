
def solution(A):
    min_avg = float('inf')
    min_pos = 0
    for i in range(len(A)):
        total = sum(A[i:])
        temp_len = (len(A)-i)
        temp_avg = total/temp_len
        if temp_avg < min_avg :
            min_pos = i
            min_avg = temp_avg
        for j in range(len(A)-1, i+1, -1):
            total -= A[j]
            temp_len -= 1
            temp_avg = total/temp_len
            if temp_avg < min_avg :
                min_pos = i
                min_avg = temp_avg
    return min_pos

print(solution([4,2,2,5,1,5,8]))


