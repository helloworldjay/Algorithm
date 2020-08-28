# 문제를 잘못읽어 시간낭비가 엄청났다..
# 공백이 들어가면 다음 문자를 넣는 것이 아니라 아예 그 쌍 자체를 버려야 한다.
# 구해야 하는 값 = 자카드 유사도
def J(set1, set2):
    # 둘다 비어있는 집합이면 결과가 1이 된다.
    if not set1 and not set2:
        return 1
    # 넘겨받은 set를 이용해서 자카드 유사도를 구한다.
    # 자카드 유사도가 (교집합 길이 / 합집합 길이) 이므로 교집합 길이만 구하면 된다.
    # 문자열의 길이가 최대 1000이므로 set의 최대 개수는 최대 999개이고 
    # O(N^2) 에도 1000000 이므로 충분히 커버 가능한 속도가 된다.
    intersection = 0
    checked = [False] * len(set2)
    for i in range(len(set1)):
        for j in range(len(set2)):
            # set1의 첫번째 글자가 set2의 첫번째 글자보다 뒤에 있는 글자면 더 비교해볼 의미가 없다.
            # break를 넣어줘야 겹치는 문자가 있을 경우 중복되지 않는다.
            if set1[i] == set2[j] and not checked[j]:
                checked[j] = True
                intersection += 1
                break
    
    return intersection/(len(set1)+len(set2)-intersection)


def solution(str1, str2):
    # 입력받은 string 값을 이 함수에서 set로 만들어 J함수에 넘겨준다.
    # 우선 전부 소문자로 만들어 준 뒤, 공백, 특수문자를 무시하며 2개씩 나누어 저장한다.
    str1, str2 = str1.lower(), str2.lower()
    set1, set2 = [], []
    idx = 0
    # 2개씩 묶을 임시 리스트
    temp = []
    # str1
    while idx < len(str1):
        # str1[idx]의 ord 값이 97이상 122 이하면 temp에 추가
        if 97 <= ord(str1[idx]) <= 122:
            temp.append(str1[idx])
            # temp의 길이가 2이면 set에 추가하고 temp의 1번 인덱스값만 temp에 넣어주는 초기화 진행
            if len(temp) == 2 :
                set1.append(temp)
                temp = [temp[1]]  
        else :
            temp = []
        # idx 1 증가
        idx += 1
        
        
    idx2 = 0
    temp2 = []
    # str2   
    while idx2 < len(str2):
        # str2[idx]의 ord 값이 97이상 122 이하면 temp에 추가
        if 97 <= ord(str2[idx2]) <= 122:
            temp2.append(str2[idx2])
            if len(temp2) == 2 :
                set2.append(temp2)
                temp2 = [temp2[1]]
        else :
            temp2 = []
        # idx 1 증가
        idx2 += 1
        # temp의 길이가 2이면 set에 추가하고 temp의 1번 인덱스값만 temp에 넣어주는 초기화 진행
        # idx가 len(str1)인데 temp가 비어있지 않으면 set에 temp 추가
        
    return int(J(set1, set2)*65536)

