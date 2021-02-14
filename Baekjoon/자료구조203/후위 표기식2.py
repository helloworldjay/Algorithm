from sys import stdin

input = stdin.readline
n = int(input())
opers = input().strip()
stack = []
target = [0 for _ in range(26)] # [1,2,3,4,5]
oper4 = ["+", "-", "*", "/"]
for i in range(n):
    target[i] = int(input().strip())
for oper in opers:
    if oper in oper4:
        a = stack.pop()
        b = stack.pop()
        if oper == "+":
            stack.append(b + a)
        elif oper == "-":
            stack.append(b - a)
        elif oper == "*":
            stack.append(b * a)
        elif oper == "/":
            stack.append(b / a)
    else:
        if oper.isdigit():
            stack.append(oper)
        else:
            stack.append(target[ord(oper)-ord('A')])
print(f'{stack[0]:.2f}')