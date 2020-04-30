from sys import stdin
n = int(stdin.readline()) # 회사 출입 기록
worklist = dict() # 회사에서 일하고 있는 사람
for _ in range(n):
    name, work = stdin.readline().strip().split()
    if work == "enter":
        worklist[name] = 1
    else :
        worklist[name] = 0    
working = sorted(worklist.items(), key= lambda x : x[0], reverse = True)
for nme, status in working:
    if status:
        print(nme)





# from sys import stdin
# n = int(stdin.readline()) # 회사 출입 기록
# ordlist = [] # 명령문 리스트
# oa = ordlist.append
# for _ in range(n):
#     name, work = stdin.readline().strip().split()
#     oa((name, work))
# worklist = [] # 회사에서 일하고 있는 사람
# wa = worklist.append
# wr = worklist.remove
# for i in range(len(ordlist)):
#     if ordlist[i][1] == "enter":
#         wa(ordlist[i][0])
#     else :
#         try:
#             wr(ordlist[i][0])
#         except:
#             continue
# for lst in sorted(worklist, reverse = True):
#     print(lst)
