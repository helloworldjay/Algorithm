t = int(input())
for _ in range(t):
    n, w = map(str, input().split()) # n은 횟수, w는 word

    for i in w:
        for __ in range(int(n)):
            print(i, end='')
    print()