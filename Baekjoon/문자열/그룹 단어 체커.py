def checker(s):
    ex = [s[0]] # 앞에서 이미 존재하는 알파벳
    ch = s[0]
    for i in range(1,len(s)):
        if ch != s[i]:
            ch = s[i]
            ex.append(ch)
    if len(list(set(ex))) == len(ex):
        return True
    return False
n = int(input())
words =[]
for i in range(n):
    words.append(input())
cnt = 0
for i in range(n):
    if checker(words[i]) :    
        cnt += 1
print(cnt)