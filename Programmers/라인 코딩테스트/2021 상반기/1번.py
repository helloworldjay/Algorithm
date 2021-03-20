#1
def solution(table, languages, preference):
    bestPosition = ""
    scoreBoard = {}
    for i in range(len(table)):
        tableList = list(table[i].split())
        scoreBoard[tableList[0]] = tableList[1:]
    totalScore = 0
    for position in scoreBoard.keys():
        tempScore = 0
        for i in range(len(languages)):
            if languages[i] in scoreBoard[position]:
                tempScore += (( 5 - scoreBoard[position].index(languages[i])) * preference[i])
        if bestPosition == "" or tempScore > totalScore or (tempScore == totalScore and position < bestPosition):
            totalScore = tempScore
            bestPosition = position
    return bestPosition

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],	["PYTHON", "C++", "SQL"],	[7, 5, 5]))

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]))
