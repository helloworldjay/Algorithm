from itertools import combinations 
# def solution(numbers, target):
#     idxlist = [i for i in range(len(numbers))] # idx 리스트
#     collist = []
#     coapp = collist.append
#     for i in range(1,len(idxlist)+1):
#         templist = list(combinations(idxlist,i))
#         for j in range(len(templist)):
#             coapp(templist[j])
#
#     cnt = 0 # 방법 가지수
#     for i in range(len(collist)):
#         pls = 0 # 더하기 요소
#         for j in collist[i]:
#             pls += numbers[j]
#         if 2*pls - sum(numbers) == target :
#             cnt += 1
#     return cnt

def solution2(numbers, target):
    global cnt
    cnt = 0
    search(numbers, target)
    return cnt

def search(subnumbers, subtarget):
    global cnt
    if len(subnumbers) == 0:
        cnt += 1 if subtarget == 0 else 0
    else:
        next_subnumbers = [] if len(subnumbers) == 1 else subnumbers[1:]
        search(next_subnumbers, subtarget + subnumbers[0])
        search(next_subnumbers, subtarget - subnumbers[0])



print(solution2([1,1,1,1,1],3))