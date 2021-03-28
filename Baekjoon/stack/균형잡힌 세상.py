from sys import stdin
input = stdin.readline
bracket_dict = {")":"(", "]":"["}
while True:
    text = input().rstrip()
    isCheck = False
    if text == ".":
        break
    stack = []
    for character in text:
        if character not in list(bracket_dict.keys()) and character not in list(bracket_dict.values()):
            continue
        if character in bracket_dict.values():
            stack.append(character)
        else:
            if not stack or stack[-1] != bracket_dict[character]:
                isCheck = True
                break
            stack.pop()
    if stack: isCheck = True
    print("no") if isCheck else print("yes")

