def solution(numbers, hand):
    keypad = {"1": (0, 0), "2": (0, 1), "3": (0, 2), "4": (1, 0), "5": (1, 1), "6": (1, 2), "7": (2, 0), "8": (2, 1),
              "9": (2, 2), "*": (3, 0), "0": (3, 1), "#": (3, 2)}
    left_hand, right_hand = "*", "#"
    result = ""
    left_section, right_section = ("1", "4", "7"), ("3", "6", "9")
    for number in map(str, numbers):
        if number in left_section:
            result += "L"
            left_hand = number
        elif number in right_section:
            result += "R"
            right_hand = number
        else:
            key_x, key_y = keypad[number]
            left_x, left_y = keypad[left_hand]
            right_x, right_y = keypad[right_hand]
            left_distance = abs(key_x - left_x) + abs(key_y - left_y)
            right_distance = abs(key_x - right_x) + abs(key_y - right_y)
            if left_distance > right_distance:
                result += "R"
                right_hand = number
            elif left_distance < right_distance:
                result += "L"
                left_hand = number
            else:
                if hand == "right":
                    result += "R"
                    right_hand = number
                else:
                    result += "L"
                    left_hand = number
    return result

def solution_check(x, y, z):
    return solution(x, y) == z
print(solution_check([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right", "LRLLLRLLRRL"))