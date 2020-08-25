T = int(input())
for idx in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    top = sorted(N_list)[len(N_list)//2:][::-1]
    bottom = sorted(N_list)[:len(N_list)//2]
    result = []
    for i in range(5):
        result.append(top[i])
        try :
            result.append(bottom[i])
        except:
            continue
    print(f"#{idx+1} {' '.join(list(map(str, result)))}")