from math import gcd


def solution(w, h):
    return w * h - (w + h - gcd(w, h))


def gcd(w, h):
    if h == 0:
        return w
    return gcd(h, w % h)

print(gcd(12,8))