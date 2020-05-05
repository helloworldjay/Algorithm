n = int(input())
def hanoi(n, s, m, e): # 원판의 개수, 시작점, 거치는점, 끝점
    if n == 1:
        print("{} {}".format(s, e))    
    else : # 위에 조건에서 return이 없기 때문에 else 처리를 해주어야 n이 1일때 아래가 작동 안한다.
        hanoi(n-1, s, e, m) 
        hanoi(1,s,m,e) 
        hanoi(n-1, m, s, e)
print(2**n-1)
hanoi(n,1,2,3) # 이렇게 하면 None이 안나옴
# print(hanoi(3,1,2,3)) # 이렇게하면 None 발생 왜나하면 위에 함수가 return이 아니라 값이 없는데 프린트를 해서 그럼