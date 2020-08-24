# 새로운 코드
# sum 연산을 for문 밖에서 해줌으로써 O(N^2)가 아니라 O(2N) 즉, O(N)으로 연산
# 하나씩 추가되므로 앞에 것을 하나 빼주고 뒤에 새로운 것만 더해 총 M개 유지

t = int(input())
for time in range(t):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    total = sum(N_list[:M])
    mx, mn = total, total
    for i in range(M, N):
        total += N_list[i] - N_list[i-M]
        if total > mx :
            mx = total
        if total < mn :
            mn = total
    print(f"#{time + 1} {mx-mn}")

# 예전 코드
# for문 안에 sum 이라는 O(N) 함수를 사용하여 O(N^2) 의 느린 속도로 연산된다.

# for i in range(t):
#     n, m = map(int, input().split())
#     maxnum = 0
#     minnum = 1000000
#     nlist = list(map(int, input().split()))
#     for j in range(n-m+1):
#         total = sum(nlist[j:j+m])
#         if total > maxnum :
#             maxnum = total
#         if total < minnum :
#             minnum = total
#     print("#{} {}".format(i, maxnum-minnum))