from sys import stdin
input = stdin.readline
n = int(input())
member = []
for _ in range(n):
    age, name = input().rstrip().split()
    member.append((int(age), name))
member.sort(key = lambda x : x[0])
for age, name in member:
    print(age, name)