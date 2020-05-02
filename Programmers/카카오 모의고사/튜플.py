def solution(s):
    a = s[2:-2].split('},{')
    for i in range(len(a)):
        a[i] = list(map(int, a[i].split(',')))
    a.sort(key = len)
    result = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] not in result:
                result.append(a[i][j])
    return result

print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))