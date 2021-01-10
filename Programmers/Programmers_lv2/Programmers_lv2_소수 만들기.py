def check_prime(num: int) -> bool:
    import math
    for check_num in range(2, int(math.sqrt(num)) + 1):
        if num % check_num == 0:
            return False
    return True


def solution(nums: list) -> int:
    cnt = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if check_prime(nums[i] + nums[j] + nums[k]):
                    cnt += 1
    return cnt
