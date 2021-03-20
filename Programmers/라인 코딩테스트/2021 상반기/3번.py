#3
def solution(enter, leave):
    peopleMet = [0 for _ in range(len(enter))]
    hadleft = [False for _ in range(len(enter))]
    officeRoom = []
    def checkPossibleToLeave(person):
        checkTemp = leave[:leave.index(person)]
        for k in range(len(checkTemp)):
            if not hadleft[checkTemp[k] - 1] or (checkTemp[k] not in officeRoom):
                return False
        return True
    for i in range(len(enter)):
        for j in range(len(officeRoom)):
            peopleMet[officeRoom[j]-1] += 1
            peopleMet[enter[i]-1] += 1
        officeRoom.append(enter[i])
        tempLeft = []
        for k in range(len(officeRoom)-1, -1, -1):
            if not checkPossibleToLeave(officeRoom[k]):
                tempLeft.append(officeRoom[k])
            else:
                hadleft[officeRoom[k]-1] = True
        officeRoom = tempLeft[:]
    return peopleMet


print(solution([1,3,2], [1,2,3]))
print(solution(	[1, 4, 2, 3], [2, 1, 3, 4]))