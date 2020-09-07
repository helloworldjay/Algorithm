# 진법 변환 함수
def numeral(n, number):
    num = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    q = number
    r = 0
    result = []
    if q == 0:
        return "0"
    while q !=  0:
        q, r = divmod(number,n)
        number = q
        result.append(num[r])
    return ''.join(result[::-1])


def solution(n, t, m, p):
    result = ""
    temp = ""
    for i in range(7200):
        temp += numeral(n, i)
    k = 0
    while t > 0:
        result += temp[(p-1)+m*k]
        k += 1
        t -= 1
    return result

# print(numeral(16,0))
print(solution(2,4,2,1))

