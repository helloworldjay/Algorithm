# 사용자가 숫자를 입력하면 숫자의 각 자릿수의 합을 구해서 반환하는 프로그램을 작성하십시오.
 

# 예를 들어 123을 입력하면 1 + 2 + 3 = 6의 결과를 반환합니다.

n = int(input())
total = 0
while n :
    total += n%10
    n = n//10
print(total)


# 위처럼 계산할 필요가 없는 이유가 input데이터는 string으로 들어오고 어차피 1자리씩 끊어서 해석하므로 각 자리를 index로 탐색하며 더해나가도 된다.