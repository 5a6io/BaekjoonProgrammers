from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque(list(), cacheSize)
    
    for c in cities:
        city = c.lower()
        if city not in cache:
            cache.append(city)
            answer += 5
        else:
            cache.remove(city)
            cache.append(city)
            answer += 1
    
    return answer