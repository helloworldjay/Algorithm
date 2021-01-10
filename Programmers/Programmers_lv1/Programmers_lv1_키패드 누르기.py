def solution(numbers, hand):
    keypad = {"1": (0, 0), "2": (0, 1), "3": (0, 2), "4": (1, 0), "5": (1, 1), "6": (1, 2), "7": (2, 0), "8": (2, 1),
              "9": (2, 2), "*": (3, 0), "0": (3, 1), "#": (3, 2)}
    # 최초의 손의 위치 설정(왼손은 *, 오른손은 #)
    left_hand, right_hand = "*", "#"
    # 정답을 저장할 result 문자열 생성
    result = ""
    # numbers를 순회하며 체크
    for number in map(str,numbers):
        # number가 1, 4, 7이면 왼손 위치를 이동 후 result에 L 추가
        if number in "147":
            left_hand = number
            result += "L"
        # number가 3, 6, 9이면 오른손 위치를 이동 후 result에 R 추가
        elif number in "369":
            right_hand = number
            result += "R"
        # number가 2, 5, 8, 0이면 왼손 위치, 오른손위치와의 거리를 계산하여
        else:
            right_distance = abs(keypad[number][0] - keypad[right_hand][0]) + abs(
                keypad[number][1] - keypad[right_hand][1])
            left_distance = abs(keypad[number][0] - keypad[left_hand][0]) + abs(
                keypad[number][1] - keypad[left_hand][1])
            # 짧은 것을 이동 후 result에 추가
            if right_distance < left_distance or (right_distance == left_distance and hand == "right"):
                right_hand = number
                result += "R"
            elif right_distance > left_distance or (right_distance == left_distance and hand == "left"):
                left_hand = number
                result += "L"
    return result

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))