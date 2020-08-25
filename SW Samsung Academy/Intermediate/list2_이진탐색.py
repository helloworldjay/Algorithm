def binary_search(target, counts, start, end):
    c = int((start + end)/2)
    # target과 만났을 때, count 출력
    if c == target:
        return counts
    # 검색을 한번 추가하므로 counts를 1 증가시킨다.
    elif c > target :
        return binary_search(target, counts+1, start, c)
    else :
        return binary_search(target, counts+1, c, end)


T = int(input())
for idx in range(T):
    # P = 책의 쪽수, A = A가 찾아야할 페이지, B = B가 찾아야할 페이지
    P, A, B = map(int, input().split())
    pa = binary_search(A, 1, 1, P)
    pb = binary_search(B, 1, 1, P)
    print(pa, pb)
    if pa == pb :
        print(f"#{idx + 1} 0")
    elif pa > pb :
        print(f"#{idx + 1} B")
    else:
        print(f"#{idx + 1} A")


