n, m = map(int, input().split())
arry = [] # 주어진 배열
for _ in range(n):
    arry.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        
k = int(input()) # 합을 구할 부분의 개수
result = []


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