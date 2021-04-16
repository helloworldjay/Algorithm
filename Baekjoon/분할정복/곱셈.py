from sys import stdin
input = stdin.readline
a, b, c = map(int, input().split())
def power(x, y, z):
    if y == 1:
        return x % z
    partial = (power(x, y // 2, z)) % z
    if y % 2 == 0:
        return (partial * partial) % z
    else:
        return ((partial) * (partial) * (x % z)) % z
print(power(a, b, c))