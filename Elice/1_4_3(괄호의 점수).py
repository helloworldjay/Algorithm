def getParenthesisScore(st):
    '''
    ()를 찾는다 -> 1로 만들어준다.
    11이 붙어있으면 더해준다.->2로 만들어준다.
    (숫자)이면 숫자*2로 변환해준다.
    '''
    st = st.replace("()", "1")
    print(st)

def main():
    examples = ["()()(())", "(()(()))", "((()())())", "()", "((()))()"] # 4, 6, 10, 1, 5 점이 나와야 합니다.
    for example in examples:
        print(example, getParenthesisScore(example))
    
if __name__ == "__main__":
    main()




# def getParenthesisScore(st):
#     score = 0
#     # 만약 st = "()" 면 1을 반환
#     if st == "()":
#         return 1
#     # 위의 경우가 아니면 조건을 찾아 들어간다.
#     # st는 올바른 괄호문자열이므로 무조건 첫번째 값은 (이고 마지막은 )가 된다.
#     # 만약 2번째가 (이며 동시에 마지막 요소 전 요소가 )이면 두 요소를 제거하고 
#     # 제거한 요소로 점수를 계산한 뒤 그 결과값에 2를 곱해준다.
#     if st[1] == "(" and st[-2] == ")":
#         st = st[1:-1]
#         score = getParenthesisScore(st)*2
#     # 위 조건을 빠져나왔단 것은 앞이나 뒤에 반드시 ()의 구조가 있다는 것이다.
#     # 그래서 조건을 제거해 나가면 앞에 두 항목이 ()거나 맨 뒤의 항목이 ()라면 
#     # 그 요소를 제거해준 값으로 다시 계산해주고 점수에 1점을 더해준다.
#     elif st[:2] == "()":
#         st = st[2:]
#         score = getParenthesisScore(st) + 1
#     elif st[-2:] == "()":
#         st = st[:-2]
#         score = getParenthesisScore(st) + 1
#     # 그리고 점수를 출력한다.
#     return score
