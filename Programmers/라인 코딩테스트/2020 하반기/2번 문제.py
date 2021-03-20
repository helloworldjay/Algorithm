from collections import deque
def solution(ball, order):
    ball = deque(ball)
    result = []
    idx = 0
    while order:
        next_ball = order[idx]
        if ball[0] == next_ball:
            result.append(ball.popleft())
            del order[idx]
            idx = 0
        elif ball[-1] == next_ball:
            result.append(ball.pop())
            del order[idx]
            idx = 0
        else: idx +=1
    return result
print(solution([1, 2, 3, 4, 5, 6], [6, 2, 5, 1, 4, 3]))