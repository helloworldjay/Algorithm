from sys import stdin
num = int(stdin.readline().rstrip())
lst = {} #회사에 있는 사람 목록
for _ in range(num):
    name, check = stdin.readline().rstrip().split()
    if check == "enter":
        lst[name] = check
    elif check == "leave":
        lst[name] = check
dict_item = list(lst.items())
for j in range(len(dict_item)):
    name2, status = dict_item[j]
    if status == "enter":
        print(name2)
