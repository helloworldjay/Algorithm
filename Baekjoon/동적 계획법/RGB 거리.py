n = int(input())
RGB = [[] for _ in range(n+1)]
for i in range(1,n+1):
    r,g,b = map(int, input().split())
    RGB[i] = [r,g,b]
for i in range(2, n+1):
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2]) + RGB[i][0] # red
    RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2]) + RGB[i][1] # green
    RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1]) + RGB[i][2] # blue
print(min(min(RGB[i][0],RGB[i][1]),RGB[i][2]))