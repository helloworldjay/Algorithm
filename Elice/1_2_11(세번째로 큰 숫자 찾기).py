
def thirdMax(nums):
    r1, r2, r3 = 0,0,0
    for i in range(len(nums)):
        if nums[i] > r1 :
            r1, r2, r3 = nums[i], r1, r2
        elif nums[i] > r2 :
            r2, r3 = nums[i], r2
        elif nums[i] > r3 :
            r3 = nums[i]
    return r3

def main():
    print(thirdMax([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23])) # should return 34

if __name__ == "__main__":
    main()
