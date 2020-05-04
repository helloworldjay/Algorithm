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

# set를 이용해서 해결
# def solution(s):
#     a = s[2:-2].split('},{')
#     for i in range(len(a)):
#         a[i] = list(map(int, a[i].split(',')))
#     a.sort(key = len)
#     result = [a[0][0]]
#     for i in range(len(a)-1):
#         temp = list(set(a[i+1])-set(a[i]))
#         result.append(temp[0])
#     return result