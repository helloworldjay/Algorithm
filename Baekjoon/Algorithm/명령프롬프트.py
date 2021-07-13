from sys import stdin
input = stdin.readline
N = int(input())
file_name = [input().strip() for _ in range(N)]
search_word = ""
for i in range(len(file_name[0])):
    is_same = True
    criterion = file_name[0][i]
    for j in range(1, N):
        if file_name[j][i] != criterion:
            is_same = False
            break
    search_word += criterion if is_same else "?"
print(search_word)

