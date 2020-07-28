
# 시간복잡도가 아니라 공간복잡도를 고려해야하는 문제

# 시간복잡도 실패
# def moveZerosToEnd(nums):
#     isCheck = False
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             for j in range(i+1, len(nums)):
#                 if nums[j] != 0:
#                     nums[i], nums[j] = nums[j], nums[i]
#                     break
#                 if j == len(nums)-1:
#                     isCheck = True
#         if isCheck :
#             break
#     return nums

# 공간복잡도 실패
# def moveZerosToEnd(nums):
#     sortednums = [0 for _ in range(len(nums))]
#     idx = 0
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             sortednums[idx] = nums[i]
#             idx += 1    
#     return sortednums


def moveZerosToEnd(nums):
    cpos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[cpos] = nums[i]
            if cpos != i :
                nums[i] = 0
            cpos += 1
    return nums


def main():
    print(moveZerosToEnd([0, 8, 0, 37, 4, 5, 0, 50, 0, 34, 0, 0]))

if __name__ == "__main__":
    main()
