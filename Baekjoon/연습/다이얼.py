# 알파벳 별로 번호 저장할 리스트 필요 idx가 번호, 저장된 알파벳이 요소
# string을 입력받아 하나씩 꺼내며 리스트에서 그 알파벳이 존재하면 인덱스를 출력한다.

alpha = [[],[], ['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]

word = input() # 할머니가 외운 단어
sec = 0 # 시간 초기값
for i in word:
    for j in range(len(alpha)):
        if i in alpha[j] :
            sec += j + 1 # 1이 2초가 걸리므로 번호보다 1 큰 수 더해주기
print(sec)