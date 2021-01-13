def find_index(s1, s2):  # 겹쳐지는 인덱스를 반환
    for i in range(len(s1)):
        index = 0
        while True:
            if s1[i + index] == s2[index]:
                if i + index >= len(s1) - 1 or index >= len(s2) - 1:
                    return i
                index += 1
                continue
            break
def solution(s1, s2):
    s1_first = s1[:find_index(s1, s2)] + s2
    s2_first = s2[:find_index(s2, s1)] + s1
    if len(s1_first) < len(s2_first):
        return s1_first
    elif len(s2_first) < len(s1_first):
        return s2_first
    return (sorted([s1_first, s2_first])[0])

print(solution("AxA", "AyA"))