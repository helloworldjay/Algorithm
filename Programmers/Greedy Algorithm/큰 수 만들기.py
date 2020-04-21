def solution(number, k):
    answerlist = [] # 답을 담을 리스트
    
    numberlist = list(map(int, list(number))) # 받은 문자열을 리스트로 저장
    selectnum = len(numberlist)- k # number의 자릿수 중 선택하는 자릿수
    maxindex = 0 # 초기화
    while selectnum > 0:
        maxlist = numberlist[maxindex:-(selectnum-1)+1] # 최대값을 찾아야 하는 리스트
        maxnum = max(maxlist) # 뒤에 자리를 뺀 수 중 가장 큰 수
        maxindex = numberlist.index(maxnum)
        answerlist.append(maxnum)
        selectnum -= 1
    return ''.join(list(map(str, answerlist))) 

print(solution("1924", 2))


