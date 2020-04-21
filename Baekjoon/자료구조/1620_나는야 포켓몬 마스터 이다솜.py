import sys
poke_num, quest = map(int, sys.stdin.readline().strip().split())
poke_dict_num = {}
poke_dict_name = {}
for i in range(1, poke_num + 1):
        name = sys.stdin.readline().strip()
        poke_dict_num[i] = name
        poke_dict_name[name] = i
for j in range(quest):
    qst = sys.stdin.readline().strip()
    try:
        print(poke_dict_num[int(qst)])
    except:
        print(poke_dict_name[qst])
