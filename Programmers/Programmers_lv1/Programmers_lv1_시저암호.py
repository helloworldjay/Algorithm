#아스키코드 ,ord()
def solution(s, n):
    arr = list(s)
    for i in range(len(arr)):
        if arr[i] == ' ' :
            continue
        else :
            num = ord(arr[i])
            if 65<=num<=90 and num+n > 90:
                num += n - 26
                arr[i] = chr(num)
            elif 90 < num <123 and num+n > 122:
                num += n - 26
                arr[i] = chr(num)
            else :
                num += n
                arr[i] = chr(num) 
    return ''.join(arr)

print(solution("a B z", 4))