from sys import stdin
input = stdin.readline
target = input().strip() # 가고 싶은 채널
broken_num = int(input()) # 고장난 채널 개수
broken = list(map(int, input().split())) # 고장난 채널 번호
button = [i for i in range(0,10) if i not in broken] # 고장나지 않은 채널 번호
# +, - 로만 채널 이동하는 경우
min_cnt = abs(100-int(target))
# 숫자로 이동하는 경우
for num in range(1000000):
    num = str(num)
    for i in range(len(num)):
        if int(num[i]) not in button: break
        elif i == len(num)-1:
            min_cnt = min(min_cnt, len(num)+abs(int(num)-int(target)))
print(min_cnt)

# 틀림
# closest = "" # 버튼으로 접근 가능한 가장 가까운 수
# if broken_num == 10 :
#     print(abs(int(target)-100))
# else :
#     for i in range(len(target)):
#         diff = 0 # 관찰할 차이
#         while True:
#             if int(target[i])+diff in button:
#                 closest += str(int(target[i])+diff)
#                 break
#             elif int(target[i])-diff in button:
#                 closest += str(int(target[i])-diff)
#                 break
#             diff += 1
#     withoutbutton = abs(100 - int(target))
#     withbutton = len(target) + abs(int(target)-int(closest))
#     print(min(withoutbutton, withbutton))