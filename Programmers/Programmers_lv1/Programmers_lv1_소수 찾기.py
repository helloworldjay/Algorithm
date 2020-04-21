# 속도, 정확성 실패
# def solution(n):
#     cnt = 0
#     if n == 2 :
#         return 1
#     elif n == 3 :
#         return 2
#     else :
#         for i in range(4, n+1):
#             if i % 6 != 1 and i % 6 != 5:
#                 continue
#             else :
#                 for j in range(2,i):
#                     if j < i-1 and i % j == 0:
#                         continue
#                     elif j == i-1 :
#                         if i % j != 0 :
#                             cnt +=1
                    
#         return cnt + 2

# print(solution(5))    

#시간 초과 실패   
# def isPrime(n):
#     isCheck = True
#     i = 2
#     if n == 2 or n == 3:
#         return True
#     else :
#         while i*i<=n:
#             if n%i==0:
#                 isCheck = False
#                 break
#             i += 1
#         return isCheck

# def solution(n):
#     cnt = 0
#     if n == (2 or 3):
#         cnt = n-3
#     else :
#         for i in range(4, n+1):
#             if i % 6 == 1 or i % 6 == 5 :
#                 if isPrime(i) == True :
#                     cnt += 1
#     return cnt + 2

# print(solution(5))

def isPrime(n):
    isCheck = True
    i = 2
    if n == 2 or n == 3:
        return True
    else :
        while i*i<=n:
            if n%i==0:
                isCheck = False
                break
            i += 1
        return isCheck

def solution(n):
    cnt = 0
    if n == (2 or 3):
        cnt = n-3
    else :
        k = 1
        while 6*k - 1 <= n:
            if isPrime(6*k-1) :
                cnt += 1
            k += 1
        
        l = 1
        while 6*l + 1 <= n:
            if isPrime(6*l+1) :
                cnt += 1
            l += 1
            
    return cnt + 2

print(solution(10))
