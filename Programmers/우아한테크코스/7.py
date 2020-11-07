def solution(n, horizontal):
    sec = 0
    visited_sec = [[0 for i in range(n)] for j in range(n)]
    row, col = 0, 0
    # horizontal이 True이면
    # 무한반복
    if horizontal == True:
        while True:
            if (row+col)%2==0: # row+col이 짝수이면
                if col != n-1 : col += 1 # col이 n-1이 아니면 오른쪽 한칸 가고 마킹한 후 왼쪽 아래로 움직인다    
                else: row += 1 # col이 n-1이면 아래로 한칸 가고 마킹한 후 왼쪽 아래로 내려간다.
                sec += 1
                visited_sec[row][col] = sec
                while True:
                    if row == n-1 or col == 0 : break 
                    row += 1
                    col -= 1
                    sec += 2
                    visited_sec[row][col] = sec
            else: # row+col이 홀수이면
                if row != n-1 : row += 1 # row가 n-1이 아니면 아래로 한칸
                else : col += 1 # row가 n-1이면 오른쪽으로 한칸
                sec += 1
                visited_sec[row][col] = sec
                while True:
                    if col == n-1 or row == 0 : break
                    row -= 1
                    col += 1
                    sec += 2
                    visited_sec[row][col] = sec
            if row == n-1 and col == n-1: return visited_sec  
    else: # horizontal이 False이면
        while True:
            if (row+col)%2!=0: # row+col이 홀수이면
                if col != n-1 : col += 1 # col이 n-1이 아니면 오른쪽 한칸     
                else: row += 1 # col이 n-1이면 아래로 한칸 
                sec += 1
                visited_sec[row][col] = sec
                while True:
                    if row == n-1 or col == 0 : break 
                    row += 1
                    col -= 1
                    sec += 2
                    visited_sec[row][col] = sec
            else: # row+col이 짝수이면
                if row != n-1 : row += 1
                else : col += 1
                sec += 1
                visited_sec[row][col] = sec
                while True:
                    if col == n-1 or row == 0 : break
                    row -= 1
                    col += 1
                    sec += 2
                    visited_sec[row][col] = sec
            if row == n-1 and col == n-1: return visited_sec
print(solution(5, False))

