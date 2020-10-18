from sys import stdin
input = stdin.readline
N = int(input())
paper = [ list(map(int, input().split())) for _ in range(N) ] # 종이를 입력
cnt_1, cnt0, cnt1 = 0, 0, 0 # -1 종이의 개수, 0 종이의 개수, 1 종이의 개수
def check_paper(paper):
    num = paper[0][0]
    for i in range(len(paper)):
        for j in range(len(paper)):
            if paper[i][j] != num:
                return -2
    return num
def split_paper(paper):
    global cnt_1, cnt0, cnt1
    if check_paper(paper) == -2:
        split_len = len(paper)//3
        for i in range(3):
            for j in range(3):
                piece = [row[j*split_len:(j+1)*split_len] for row in paper[i*split_len:(i+1)*split_len]]
                split_paper(piece) # 조각을 재검사
    elif check_paper(paper) == 1 : cnt1 += 1
    elif check_paper(paper) == 0 : cnt0 += 1
    elif check_paper(paper) == -1 : cnt_1 += 1
split_paper(paper)
for cnt in [cnt_1, cnt0, cnt1]:
    print(cnt)