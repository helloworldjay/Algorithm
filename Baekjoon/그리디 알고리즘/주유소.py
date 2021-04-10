from sys import stdin
input = stdin.readline
N = int(input())
gas_to_move = list(map(int, input().split()))
gas_price = list(map(int, input().split()))
cost = 0
current_price = gas_price[0]
temp_distance = gas_to_move[0]
for i in range(1, N):
    if i == N-1:
        cost += current_price * temp_distance
        break
    if current_price > gas_price[i]:
        cost += current_price * temp_distance
        current_price = gas_price[i]
        temp_distance = gas_to_move[i]
    else:
        temp_distance += gas_to_move[i]
print(cost)