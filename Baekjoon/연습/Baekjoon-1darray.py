
# 1

# import sys
# num = int(sys.stdin.readline()) 
# a = list(map(int,sys.stdin.readline().split()))
# if (len(a)!=num):
#     print("Wrong Input")
# else:
#     a.sort()
#     print(a[0],a[num-1])


# 2
# import sys
# a = []
# maxNum = 0
# maxIndex = 0
# for i in range(9):
#     num = int(sys.stdin.readline())
#     a.append(num)
#     if (num> maxNum):
#         maxNum = num
#         maxIndex = i
# print(maxNum, maxIndex+1, sep="\n")

# 3
# import sys
# code = input()
# if(code == "1 2 3 4 5 6 7 8"):
#     print("ascending")
# elif(code == "8 7 6 5 4 3 2 1"):
#     print("descending")
# else:
#     print("mixed")

# 4
# import sys
# num1 = int(sys.stdin.readline())
# num2 = int(sys.stdin.readline())
# num3 = int(sys.stdin.readline())
# num = str(num1*num2*num3)
# for i in range(10):
#     print(num.count(str(i)))
    
#5
import sys
num = []
for i in range(10):
    num.append(i%42)
    