s = input().upper()

set_s = list(set(s)) # 중복 제거
cntlist = []
for i in range(len(set_s)) :
    cntlist.append((set_s[i], s.count(set_s[i])))
cntlist.sort(key= lambda x : -x[1])
if len(cntlist) > 1:
    print('?') if cntlist[0][1] == cntlist[1][1] else print(cntlist[0][0])
        
else :
    print(cntlist[0][0])
   
