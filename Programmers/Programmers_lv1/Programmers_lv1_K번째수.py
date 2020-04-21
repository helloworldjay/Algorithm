def solution(array, commands):
    arr = []
    for i in range(len(commands)):
        for k,l,m in map(str,commands[i]):
            arr.append(sorted(array[int(k):int(l)+1])[int(m)-1])
    return arr

