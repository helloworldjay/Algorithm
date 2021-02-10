from sys import stdin

input = stdin.readline
n = int(input())


def checkVPS(s_list: str) -> bool:
    stack = []
    for s in s_list:
        if s == "(":
            stack.append("(")
            continue
        if not stack:
            return False
        stack.pop()
    if stack:
        return False
    return True


for _ in range(n):
    testcase = input().strip()
    print("YES" if checkVPS(testcase) else "NO")
