from sys import stdin

input = stdin.readline
prefix = "(" + input().strip() + ")"
answer = ""
stack = []

priority = {
    "*": 1,
    "/": 1,
    "+": 2,
    "-": 2
}

for letter in prefix:
    if letter.isalpha():
        answer += letter
    elif letter == ')':
        while stack:
            temp = stack.pop()
            if temp == '(':
                break
            answer += temp
    elif letter == '(':
        stack.append(letter)
    else:
        while stack[-1] != '(' and priority[letter] >= priority[stack[-1]]:
            answer += stack.pop()
        stack.append(letter)
print(answer)
