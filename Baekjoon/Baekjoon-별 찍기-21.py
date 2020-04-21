# 10996번
from sys import stdin
num = int(stdin.readline())
for _ in range(num):
    if num % 2 == 1 :
        print("* "*int((num+1)/2))
        print(" *"*(int((num+1)/2)-1))
    else :
        print("* "*int(num/2))
        print(" *"*int(num/2))