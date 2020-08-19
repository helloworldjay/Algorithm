n = int(input())
for i in range(1<<n):
    for j in range(n):
        if i&(1<<j):
            print(bin(1<<j))