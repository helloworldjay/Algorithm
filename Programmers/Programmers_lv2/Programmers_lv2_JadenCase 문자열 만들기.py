def solution(s):
    lst = list(s.lower())
    lst[0] = lst[0].upper()
    for i in range(1,len(lst)):
        if lst[i-1] != " ":
            continue
        else :
            lst[i] = lst[i].upper()
    return "".join(lst)



print(solution("3people unFollowed me"))
