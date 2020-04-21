from sys import stdin
g, q = map(int, stdin.readline().split()) # g = 걸그룹 수, q = quiz 수
ggroup = dict()
for _ in range(g):
    name = stdin.readline().strip() # 걸그룹 이름
    n = int(stdin.readline()) # 걸그룹 멤버 수
    glist = [] # 걸그룹 멤버 리스트
    ga = glist.append
    for i in range(n):
        ga(stdin.readline().strip())
    ggroup[name] = glist # 걸그룹 이름이 key, 걸그룹 멤버 리스트가 value가 되는 dict
ans = [] # 정답 리스트
aa = ans.append
for _ in range(q):
    qz = stdin.readline().strip() # 퀴즈 이름
    ty = int(stdin.readline()) # 퀴즈 종류
    if ty == 0 :
        ggroup[qz].sort()
        for nm in ggroup[qz]:
            aa(nm)
    else :
        for gp, mem in ggroup.items():
            if qz in mem:
                aa(gp)
for answer in ans:
    print(answer)
