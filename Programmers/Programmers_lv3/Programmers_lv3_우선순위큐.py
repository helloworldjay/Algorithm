# level3 스킬체크




def solution(operations):
    arry = []
    for i in range(len(operations)):
        if operations[i][0] == "I":
            if len(arry)==0: arry.append(int(operations[i][2:]))
            else :
                for j in range(len(arry)):
                    if arry[j] >= int(operations[i][2:]):
                        arry.insert(j,int(operations[i][2:]))
                        break
                    elif j == len(arry)-1: arry.append(int(operations[i][2:]))
        else:
            if len(arry) != 0:
                if operations[i][2] == "1":
                    arry.pop()
                else:
                    arry = arry[1:]
    if len(arry) == 0: return [0,0]
    else: return([arry[-1],arry[0]])

