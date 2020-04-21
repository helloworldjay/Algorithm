#7568번
from sys import stdin
answerlist = [] # 순위리스트
sizelist = []
append = sizelist.append 
append2 = answerlist.append
people = int(stdin.readline().strip())
for _ in range(people):
    append(tuple(map(int, stdin.readline().strip().split())))
for i in range(len(sizelist)):
    k = 0
    for w,h in sizelist[:i] + sizelist[i+1:]: 
        if sizelist[i][0] < w and sizelist[i][1] < h :
            k += 1
    append2(k+1)
for ans in answerlist :
    print(ans, end = " ")
