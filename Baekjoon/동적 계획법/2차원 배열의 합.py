from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
arry = [list(map(int,input().split())) for _ in range(N)]
cache = [[0 for _ in range(M+1)] for j in range(N+1)]
for i in range(N):
    temp = 0
    for j in range(M):
        temp += arry[i][j]
        cache[i+1][j+1] = temp
T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int,input().split())
    temp = 0
    for i in range(x1,x2+1):
        temp += cache[i][y2]-cache[i][y1-1]
    print(temp)





# 이렇게 구현으로 문제를 해결하면 9억 정도의 시간 복잡도가 생성

# n , m = map(int, input().split())
# arry = [] # 주어진 배열
# for _ in range(n):
#     arry.append(list(map(int, input().split())))
# k = int(input()) # 합을 구할 부분의 개수
# result = []
# for _ in range(k):
#     temp = 0
#     i, j, x, y = map(int,input().split())
#     for m in range(i-1, x):
#         for n in range(j-1, y):
#             temp += arry[m][n]
#     result.append(str(temp))    # join문은 str 리스트 요소만 가능하다.      
# print('\n'.join(result))