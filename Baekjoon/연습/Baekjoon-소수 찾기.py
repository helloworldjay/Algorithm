n, lst = input(), list(map(int, input().split())) # n = 리스트 항목의 수, lst = 주어진 리스트 
cnt = 0 # 소수의 개수
for ele in lst : # list의 element 꺼내오기
    sqrt = int(ele**(1/2)) # 소수 판별을 위해 제곱근 구하기
    # 2부터 시작해서 제곱근 까지 수 중에 나눠지는 수가 있는지 판별
    if ele >= 4 :
        for i in range(2, sqrt+1):
            if ele % i == 0:
                cnt -= 1
                break
        cnt += 1
    elif ele == 2 or ele == 3:
        cnt += 1
print(cnt)

