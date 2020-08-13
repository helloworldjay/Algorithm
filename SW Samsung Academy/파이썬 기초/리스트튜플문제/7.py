
# 다음의 결과와 같이 정수를 입력하면 리스트 내포를 이용해

# 약수 리스트를 출력하는 코드를 작성하십시오.
n = int(input())

print([i for i in range(1, n+1) if n % i == 0])