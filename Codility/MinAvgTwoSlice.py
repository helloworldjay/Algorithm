def solution(A):
    min_avg = 10001
    min_idx = -1
    for i in range(len(A)-1):
        if sum(A[i:i+2])/2 < min_avg :
            min_avg = sum(A[i:i+2])/2
            min_idx = i
        if i != len(A)-2 and sum(A[i:i+3])/3 < min_avg :
            min_avg = sum(A[i:i+3])/3
            min_idx = i
    return min_idx


# efficiency test failed
# def solution(A):
#     c_sum = [0]*(len(A)+1) # cumulative sum
#     for i in range(1, len(c_sum)):
#         c_sum[i] = c_sum[i-1] + A[i-1]
#     min_avg = float('inf')
#     min_index = 0
#     for i in range(1,len(c_sum)):
#         for j in range(i):
#             temp_avg = (c_sum[i]-c_sum[j])/i-j
#             if temp_avg < min_avg : 
#                 min_avg =temp_avg
#                 min_index = j
#     return j

print(solution([4,2,2,5,1,5,8]))


