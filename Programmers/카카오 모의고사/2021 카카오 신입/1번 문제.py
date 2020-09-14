# 33분
def solution(new_id):
    # 1단계 
    new_id = new_id.lower()
    # 2단계 
    possible = ['-','_','.']
    temp = ""
    for idx in range(len(new_id)):
        if new_id[idx].isalpha() or new_id[idx].isdecimal() or (new_id[idx] in possible): 
            temp += new_id[idx]
    new_id = temp
    # 3단계 
    if len(new_id) != 0 :
        temp = new_id[0]
        for i in range(1, len(new_id)):
            if new_id[i] == "." and temp[-1] == ".": continue
            else : temp += new_id[i]
        new_id = temp
    # 4단계 
    if len(new_id) != 0 and new_id[0] == ".": new_id = new_id[1:]
    if len(new_id) != 0 and new_id[-1] == ".": new_id = new_id[:-1]
    # 5단계 
    if len(new_id) == 0: new_id = 'a'
    # 6단계 
    if len(new_id) >= 16: new_id = new_id[:15]
    while new_id[-1] == '.':
        new_id = new_id[:-1]
    # 7단계 
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    return new_id

print(solution(	"..................."))


