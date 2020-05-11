# 두 숫자사이의 거리
def distance(num1, num2): # num1, num2는 str
    idx = []
    phone = ["123","456","789","*0#"]
    for i in range(4):
        j = phone[i].find(num1)
        j2 = phone[i].find(num2)
        if j != -1 :
            idx.append((i, j))
        if j2 != -1 :
            idx.append((i,j2))
    return abs(idx[1][0]-idx[0][0]) + abs(idx[1][1]-idx[0][1])

def solution(numbers, hand):
    # 결과를 담을 리스트
    hands = [0 for i in range(len(numbers))] 
    # 손의 최근 위치를 저장할 list 생성
    handpos = ["*", "#"] # 0 index는 왼손, 1 index는 오른손
    # 번호를 하나씩 검색
    for i in range(len(numbers)):
        num = numbers[i]
        # 번호가 1,4,7 일 경우 왼손만 사용
        if num % 3 == 1:
            hands[i] = "L"
            handpos[0] = str(num)
        # 번호가 3,6,9 일 경우 오른손만 사용
        elif num % 3 == 0 and num != 0:
            hands[i] = "R"
            handpos[1] = str(num)
        # 번호가 2,5,8,0 일 때
        else:
            leftdis = distance(handpos[0], str(num)) # 최근 왼손 위치에서 눌러야하는 번호 거리
            rightdis = distance(handpos[1], str(num)) # 최근 오른손 위치에서 눌러야하는 번호 거리
            # 왼손이 더 가까울 때
            if leftdis < rightdis :
                hands[i] = "L"
                handpos[0] = str(num)
            # 오른손이 더 가까울 때
            elif leftdis > rightdis :
                hands[i] = "R"
                handpos[1] = str(num)
            # 거리가 같을 때
            else :
                # 왼손잡이
                if hand == "left":
                    hands[i] = "L"
                    handpos[0] = str(num)
                # 오른손잡이
                else : 
                    hands[i] = "R"
                    handpos[1] = str(num)
    return ''.join(hands)
