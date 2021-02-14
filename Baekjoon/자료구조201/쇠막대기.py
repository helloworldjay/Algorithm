from sys import stdin

input = stdin.readline
s = input().strip()
s = s.replace("()", "L")
stack = []
answer = 0
for token in s:
    if token == "(":
        stack.append(token)
        answer += 1
    elif token == ")":
        stack.pop()
    else:  # Laser
        answer += len(stack)
print(answer)