def solution(n):
    cnt1 = bin(n).count('1')
    while True:
        n += 1
        if bin(n).count('1') == cnt1 :
            return n

print(solution(78))

