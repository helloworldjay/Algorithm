from sys import stdin
def check(x):
    for i in range(x):
        if row[i] == row[x]:
            return False
        if abs(row[x]-row[i]) == x-i:
            return False
    return True

def dfs(x):
    if x == n :
        result += 1
    else :
        for i in range(x):
            row[x] = i
            if check(x):
                dfs(x+1)
n = int(stdin.readline())
row = [0 for _ in range(n)] 
result = 0
dfs(0)
print(result)