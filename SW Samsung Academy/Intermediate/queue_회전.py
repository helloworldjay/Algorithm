# testcase
T = int(input())
for idx in range(T):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    # 큐의 맨 앞
    front = 0
    # 맨 앞의 인덱스를 N%M만큼 이동
    front += M%N
    # 주어진 요소를 출력
    print(f"#{idx+1} {N_list[front]}")