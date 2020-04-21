#실패한 코드 - 문제 잘못 읽음
# def solution(s):
#     slist = list(s.lower())
#     for i in range(len(slist)):
#         if i%2 ==0 :
#             slist[i] = slist[i].upper()
#     return ''.join(slist)


# def solution(s):
#     slist = s.split()
#     newlist = []
#     for i in range(len(slist)):
#         new = ''
#         for j in range(len(slist[i])):
#             if j % 2 == 0 :
#                new += slist[i][j].upper()
#             else :
#                new += slist[i][j].lower()
#         newlist.append(new)
#     return " ".join(newlist)

def solution(s):
    cnt = 0
    news = ""
    for i in s :
        if i == " " :
            cnt = 0
            news += " "
            continue
        elif cnt % 2 == 0 :
            news += i.upper()
            cnt += 1
        else :
            news += i.lower()
            cnt += 1
    return news

print(solution("try hello world"))
