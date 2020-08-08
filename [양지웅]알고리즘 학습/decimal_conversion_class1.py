
# def solution(num, ns, tt):
#     # 기저조건 num이 0일 때
    
#     if len(num) == 0 :
#         return tt
#     try :
#         tt += int(num[-1])*ns
#         num = num[:-1]
#         solution(num, ns,tt)
#     except :
#         tt += (ord(num[-1])-55)*ns  
#         num = num[:-1]
#         solution(num, ns,tt)

# st, ns = input().split()
# ns= int(ns)
# tt = 0
# print(solution(st,ns,tt))



before_str, cipher_num= input().split()
# 'ZZZZZZ', '36'
cipher_num = int(cipher_num)
decimal_result = 0
#재귀 없이 풀이
n = len(before_str)
for i in range(0, n):
    idx_char = before_str[i]
    if idx_char.isnumeric():
        decimal_result += int(idx_char) * (cipher_num ** (i))
    else:
        # 여기 복습
        decimal_result += (ord(idx_char)-ord('A')+10) * (cipher_num ** (i))

print(decimal_result)
