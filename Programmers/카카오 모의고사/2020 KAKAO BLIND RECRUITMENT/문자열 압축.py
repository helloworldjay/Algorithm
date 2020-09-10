def solution(s):
    min_len = len(s)
    for box_size in range(len(s)//2, 0, -1):
        # s를 크기 box_size로 잘라 담을 리스트
        temp = []
        q,r = divmod(len(s), box_size)
        for box_num in range(q):
            temp.append(s[box_size*box_num:box_size*(box_num+1)])
        if r !=0 : temp.append(s[-r:])
        # temp 안에 중복 요소를 체크하는 반복문
        idx = 0
        k = 1
        #결과를 담을 변수
        result = []
        while True:
            # idx번째 요소와 그 다음 관찰 요소가 같지 않을 때
            if temp[idx] != temp[idx+k]:
                # 겹치는 요소가 없었다.
                if k==1:
                    result.append(temp[idx])
                    idx += 1
                # 겹치는 요소가 있었다면
                else :
                    result.append(f"{k}")
                    result.append(temp[idx])
                    idx += k
                    k = 1
            # idx번째 요소와 그 다음 관찰 요소가 같을 때
            else :
                k += 1
                # k가 끝까지 왔으면
                if idx + k == len(temp): 
                    result.append(f"{k}")
                    result.append(temp[idx])
                    break
            if idx == len(temp)-1:
                result.append(temp[idx])
                break
        if len(''.join(result)) < min_len: min_len = len(''.join(result))
    return min_len

print(solution("ababcdcdababcdcd"))