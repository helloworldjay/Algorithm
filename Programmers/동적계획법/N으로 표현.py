def solution(N, number):
    cache = [0, {N}] # N을 0개 쓴 경우, 1개 쓴 경우로 초기화
    if N == number : return 1 # 아래에서 N을 한 번 쓰는 경우가 제외되므로 예외처리
    for i in range(2,9): # N을 2개 사용할 때부터 8개 사용할 경우를 생각
        case = {int(str(N)*i)} # N번 사용할 때 처음 연속 숫자의 경우를 넣어줌
        for j in range(1, i//2+1): # N을 1개만 사용할 때부터 중간까지(어차피 중간을 넘으면 똑같은 경우가 된다)
            for x in cache[j]:
                for y in cache[i-j]:
                    case.add(x+y)
                    case.add(x-y)
                    case.add(y-x)
                    case.add(x*y)
                    if x != 0 : case.add(y//x)
                    if y != 0 : case.add(x//y)
        if number in case: return i
        cache.append(case)
    return -1 # 8번 사용 이내에 원하는 number가 만들어지지 않았으면 -1을 출력