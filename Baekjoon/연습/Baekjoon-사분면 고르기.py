# 14681번
from sys import stdin
x = int(stdin.readline().strip())
y = int(stdin.readline().strip())
if x > 0 and y > 0 :
    print(1)
elif x < 0 and y > 0 :
    print(2)      
elif x < 0 and y < 0 :
    print(3)
else :
    print(4)