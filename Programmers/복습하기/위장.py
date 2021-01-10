def solution(clothes):
    clothes_dict = {}
    for cloth, type in clothes:
        clothes_dict[type] = clothes_dict.get(type, 0) + 1
    total = 0
    for type, num in clothes_dict.items():
        total *= (num+1)
    return total
print(solution(	[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))