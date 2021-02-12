from sys import stdin
input = stdin.readline
s = input().strip()
cnt = [0 for _ in range(26)]
for c in s:
    cnt[ord(c)-ord('a')] += 1
print(' '.join(map(str, cnt)))