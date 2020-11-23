def solution(heights:list) -> int:
    left, right = 0, len(heights)-1
    leftmax, rightmax = 0, 0
    water = 0 # 총 물의 양
    # index left가 right보다 왼쪽에 있을 동안 반복
    while left <= right:
        leftmax = max(heights[left], leftmax)
        rightmax = max(heights[right], rightmax)
        
        if leftmax <= rightmax:
            water += leftmax - heights[left]
            left += 1
        else : 
            water += rightmax - heights[right]
            right -= 1
    return water
        
print(solution([0,1,0,2,1,0,1,3,2,1,2,1]))