from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    sec = 0
    for city in cities:
        city = city.lower()
        if city not in cache:
            sec += 5
            if cacheSize != 0 and len(cache) == cacheSize:
                cache.popleft()
            if cacheSize != 0:
                cache.append(city)
        else:
            sec += 1
            for i in range(len(cache)):
                if cache[i] == city:
                    del cache[i]
                    cache.append(city)
    return sec
print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))

