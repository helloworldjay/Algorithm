#실패한 코드
# def solution(arr):
#     newarr = [arr[0]]
#     for i in range(len(arr)-1):
#         if arr[i] != arr[i+1]:
#             newarr.append(arr[i+1])
#             if i == len(arr)-2 :
#                 newarr.append(arr[i+1])   
#     return newarr

def solution(arr):
    newarr = []
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1] :
            newarr.append(arr[i])
        if i == len(arr)-2 :
            newarr.append(arr[i+1])
    return newarr

print(solution([1,1,3,3,0,1,1]))