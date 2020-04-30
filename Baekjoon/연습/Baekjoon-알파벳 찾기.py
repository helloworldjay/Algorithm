# 10809번
from sys import stdin
alphalist = [chr(i) for i in range(97,123)]
anslist = [-1 for _ in range(26)]
targetlist = list(stdin.readline().strip()) # 알파벳 모음
for i in range(len(targetlist)):
    if anslist[alphalist.index(targetlist[i])] == -1 :
        anslist[alphalist.index(targetlist[i])] = i
for i in range(len(anslist)): 
    print(anslist[i], end = " ")
