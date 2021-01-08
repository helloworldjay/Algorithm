def binary_transition(x: str) -> list:
    num_1 = 0
    for num in x:
        if num == "1": num_1 += 1
    return [str(bin(num_1))[2:], len(x) - num_1]


def solution(s: str) -> list:
    transition_cnt = 0
    total_num_0 = 0
    while s != "1":
        s, num_0 = binary_transition(s)
        total_num_0 += num_0
        transition_cnt += 1
    return [transition_cnt, total_num_0]

print(solution("110010101001"))