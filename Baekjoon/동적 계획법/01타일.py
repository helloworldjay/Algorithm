
#그냥 기본값을 최대 길이로 설정해준다.
n = int(input())
cache = [0] * 1000001
cache[1] = 1
cache[2] = 2
for i in range(3, n+1):
    cache[i] = (cache[i-1] + cache[i-2])%15746 # 나누기를 여기서 해야 입력 값 자체가 작아져서 메모리 초과가 발생하지 않는다.
print(cache[n])




# inum = int(input()) # input number
# if inum > 2:
#     cache = [0 for i in range(inum+1)] # memoization
#     cache[0] = 0
#     cache[1] = 1
#     cache[2] = 2
#     for i in range(3, inum+1):
#         cache[i] = cache[i-1] + cache[i-2]

# print(cache[inum]%15746)


# 위와 같이 짜면 속도 이슈 발생
# cache에 저장되는 값이 너무 크므로 저장할 때 저장 하는 cache 값 자체에 15746으로 나눈 나머지를 넣는다.