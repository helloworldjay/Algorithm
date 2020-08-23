# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


# O(B-A)

def solution1(A, B, K):
    ret = 0
    for dividend in range(A, B+1):
        if dividend % K == 0:
            ret += 1
    return ret

#O(1)

def solution2(A, B, K):
    quotientA = A // K
    remainderA = A % K
    quotientB = B // K
    return quotientB - quotientA + 1 if remainderA == 0 else quotientB - quotientA

