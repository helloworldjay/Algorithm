from sys import stdin
input = stdin.readline
N = int(input()) # 1<=N<=64 범위의 2의 제곱수
video = [list(map(int, list(input().strip()))) for _ in range(N)]
result = "" # 결과
def compress(arry): # 2차원 배열을 압축해주는 함수
    global result
    standard = arry[0][0] # 기준점
    for i in range(len(arry)):
        for j in range(len(arry[0])):
            if arry[i][j] != standard: # 다른게 존재하면 사분할
                result += "("
                quad(arry)
                result += ")"
                return None
    result += str(standard)
def quad(arry): # 4분할하는 함수
    n = len(arry)//2
    for i in range(2):
        for j in range(2):
            compress([row[j*n:(j+1)*n] for row in arry[i*n:(i+1)*n]])
compress(video)
print(result)

    

