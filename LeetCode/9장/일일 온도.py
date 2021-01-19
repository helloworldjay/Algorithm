from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0 for _ in range(len(T))]
        stack = []
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]: # stack 안은 역순일 수밖에 없음
                last = stack.pop()
                result[last] = i - last
            stack.append(i)
        return result
