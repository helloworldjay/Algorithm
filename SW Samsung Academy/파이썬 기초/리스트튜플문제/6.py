# 다음의 결과와 같이 정수를 입력하면 약수를 리스트에 추가해 출력하는 코드를 작성하십시오.
import math

num = int(input())
sqrtn = int(math.sqrt(num))
factor = []
for i in range(1, sqrtn+1):
    if num % i == 0:
        factor.append(i)
        if num//i not in factor:
            factor.append(num//i)
print(sorted(factor))
