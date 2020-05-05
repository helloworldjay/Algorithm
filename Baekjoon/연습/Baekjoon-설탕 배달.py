# 2839번
n = int(input())
n5 = n // 5
checker = 0
while n5 > -1:
    if (n - n5*5) % 3 == 0:
        checker = n5 + (n - n5*5) // 3
        break
    else :
        n5 -= 1
print(checker) if checker else print(-1)



# 이렇게 하면 5 1개 3 2개 이런 경우가 안됨
# n = int(input())
# a = n // 5  
# b = n % 5 
# if b % 3 == 0:
#     print(a + b//3)
# else : 
#     print(n//3) if n % 3 == 0 else print(-1)
    