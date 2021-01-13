def solution(n: int) -> int:
    box_3, box_5 = 0, n // 5
    while box_5 >= 0:
        if (n - 5 * box_5) % 3 == 0:
            box_3 = (n - 5 * box_5) // 3
            return box_3 + box_5
        box_5 -= 1
    return -1

    # box_num = -1
    # while 5 * box_5_cnt <= n:
    #     box_5 = n // 5
    #     if (n % 5) % 3 == 0:
    #         box_3 = (n % 5) // 3
    #         box_num = box_3 + box_5
    #     box_5_cnt += 1
    # return box_num


print(solution(21))
