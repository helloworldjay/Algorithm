def solution(absolutes, signs):
    return sum([absolutes[i] for i in range(len(absolutes)) if signs[i] == True]) - sum([absolutes[i] for i in range(len(absolutes)) if signs[i] == False])