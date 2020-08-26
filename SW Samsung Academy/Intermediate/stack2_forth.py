# testcase 입력
T = int(input())
# testcase를 반복하며 입력 받기
for idx in range(T):
    # 빈 스택을 생성
    stack = []
    # 연산할 연산을 입력받아 리스트로 만들기
    testcase = list(input().split())
    # testcase를 순회하며 연산하기 
    for i in range(len(testcase)):
        if testcase[i].isdecimal() :
            # 성공하면 testcase는 숫자이다.
            num =  int(testcase[i])
            stack.append(num)
        # testcase가 연산자라면
        else:
            # .이 나왔을 때 스택에 요소가 있다면 요소를 출력한다.
            if testcase[i] == '.' :
                if len(stack) == 1:
                    print(f"#{idx+1} {stack[-1]}")
                else :
                    print(f"#{idx+1} error")
                break
            # 스택에 숫자 2개 이하가 존재하면 에러
            elif len(stack) < 2:
                print(f"#{idx+1} error")
                break
            # 연산자가 나오면 연산결과를 다시 stack에 넣는다.
            stack1 = stack.pop()
            stack2 = stack.pop()
            if testcase[i] == "+":
                stack.append(stack2 + stack1)
            elif testcase[i] == "-":
                stack.append(stack2 - stack1)
            elif testcase[i] == "*":
                stack.append(stack2 * stack1)
            elif testcase[i] == "/":
                stack.append(stack2 // stack1)

