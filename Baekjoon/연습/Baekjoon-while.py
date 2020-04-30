#1

# import sys
# isCheck = True
# while(isCheck):
#     num1 , num2 = map(int, sys.stdin.readline().split())
#     if((num1 and num2) == 0):
#         isCheck = False
#     else :
#         print(num1 + num2)



#2 EOF의 개념 (End of File)

# import sys
# while(True):
#     try:
#         num1 , num2 = map(int, sys.stdin.readline().split())
#         print(num1 + num2)
#     except:
#         break
    
#3 

# import sys
# num = int(sys.stdin.readline())
# cnt = 0
# num10 = num//10
# num1 = num%10
# while(True):    
#     sum = num10 + num1
#     sum1 = sum%10
#     num10 = num1
#     num1 = sum1
#     cnt += 1
#     if((num10 * 10 + num1) == num):
#         print(cnt)
#         break
