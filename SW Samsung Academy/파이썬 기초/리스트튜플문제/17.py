
# 다음의 결과와 같이 사용자로부터 콤마(,)로 구분해 여러 원의 반지름을 입력 받아


# 이들에 대한 원의 둘레를 계산해 출력하는 프로그램을 작성하십시오.




import math
r = list(map(int, input().split(', ')))
p = math.pi
area_size= [ str(round(p * i * 2,2)) for i in r]
print(', '.join(area_size))


# join은 string만 가능



