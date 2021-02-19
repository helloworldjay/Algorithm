from sys import stdin

input = stdin.readline
while True:
    cnt = [0 for _ in range(4)]
    string = input().rstrip('\n')
    if not string:
        break
    for s in string:
        if s.islower():
            cnt[0] += 1
        elif s.isupper():
            cnt[1] += 1
        elif s.isdigit():
            cnt[2] += 1
        elif s.isspace():
            cnt[3] += 1
    print('{} {} {} {}'.format(cnt[0],cnt[1],cnt[2],cnt[3]))
# 백준은 f-string 사용 불가 with pypy
