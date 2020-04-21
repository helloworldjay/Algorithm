from sys import stdin

num, price = map(int, stdin.readline().rstrip().split()) # 동전 종류의 수, 금액 입력
type_coin = [] # 동전 종류 리스트
for i in range(num):
    coin = int(stdin.readline()) # 코인 종류 오름차순 입력
    type_coin.append(coin) #코인 종류 리스트에 추가
type_coin.sort(reverse = True) # 코인 순서 뒤집기
num_coin = 0 # 동전 개수
lst_number = 0
while True :
    num_coin += (price // type_coin[lst_number])
    price %= type_coin[lst_number]
    if price == 0 or lst_number == num - 1:
        break
    lst_number += 1
print(num_coin)
