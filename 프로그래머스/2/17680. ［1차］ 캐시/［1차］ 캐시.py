def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = str.lower(city)
        if city not in cache:
            if len(cache) == cacheSize:
                cache.pop(0)
            answer += 5
            cache.append(city)
        else:
            cache.remove(city)
            cache.append(city)
            answer += 1
    return answer