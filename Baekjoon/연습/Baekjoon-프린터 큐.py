from collections import deque
t = int(input()) # testcase 
for _ in range(t):
    n,m = map(int,input().split())
    queue = list(map(int,input().split()))
    queue = deque([(i, idx) for idx, i in enumerate(queue)])
    cnt = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x : x[0])[0]:
            cnt += 1
            if queue[0][1] == m :
                print(cnt)
                break
            else :
                queue.popleft()
        else :
            queue.append(queue.popleft())
        
       




     
    
    