# 26분
def seperate(file):
    head, number, tail = "", "", ""
    is_check_head = True
    is_check_tail = True
    cnt = 5
    for char in range(len(file)):
        # 숫자가 아니고 head가 켜져 있으면
        if not file[char].isdecimal() and is_check_head:
            head += file[char]
        elif file[char].isdecimal() and is_check_tail:
            # 이제 head에 안들어감
            is_check_head = False
            number += file[char]
            cnt -= 1
            if cnt == 0:
                is_check_tail = False
        else :
            tail = file[char:]
            break
    return (head, number, tail)


def solution(files):
    for i in range(len(files)):
        files[i] = seperate(files[i])
    files.sort(key = lambda x : (x[0].lower(),int(x[1])))
    for i in range(len(files)):
        files[i] = ''.join(files[i])
    return files

print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
