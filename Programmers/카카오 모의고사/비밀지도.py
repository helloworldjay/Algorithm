def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        if len(bin(arr1[i])) < 2 + n :
            arr1[i] = "0"*(n-(len(bin(arr1[i]))-2)) + bin(arr1[i])[2:]
        else :
            arr1[i] = bin(arr1[i])[2:]
        if len(bin(arr2[i])) < 2 + n :
            arr2[i] = "0"*(n-(len(bin(arr2[i]))-2)) + bin(arr2[i])[2:]
        else :
            arr2[i] = bin(arr2[i])[2:]
    for i in range(n):
        temp = ""
        for j in range(n):
            if arr1[i][j] == "1" or arr2[i][j] == "1":
                temp += "#"
            else : 
                temp += " "
        answer.append(temp)
    return answer
solution(5, [9, 20, 28, 18, 11],[30, 1, 21, 17, 28])