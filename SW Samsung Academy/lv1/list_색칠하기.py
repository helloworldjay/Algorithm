t = int(input()) #testcase의 수
for i in range(t):
    n = int(input()) #색칠할 수 
    baselist = [[0]*10]*10
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        if color == 1 :
             
