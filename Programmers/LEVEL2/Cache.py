# 45. 캐시

'''
LRU(Least Recently Used)알고리즘 : 가장 최근에 사용되지 않은 것 즉, 가장 오래전에 사용한 것을 제거하는 알고리즘
오랫동안 사용하지 않았던 데이터는 앞으로도 사용할 확률이 적다.
'''
def solution(cacheSize, cities):
    answer = 0

    cache = []
    cities = [city.lower() for city in cities]
    if cacheSize != 0:
        for city in cities:
            if city in cache:
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1
            else:
                if len(cache) < cacheSize:
                    cache.append(city)
                    answer += 5
                else:
                    cache.pop(0)
                    cache.append(city)
                    answer += 5
    else:
        answer += len(cities) * 5

    return answer

cacheSize_1 = 3
cacheSize_2 = 3
cacheSize_3 = 2
cacheSize_4 = 5
cacheSize_5 = 2
cacheSize_6 = 0

cities_1 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
            "Jeju", "Pangyo", "Seoul", "NewYork", "LA"
            ]
cities_2 = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo",
            "Seoul", "Jeju", "Pangyo", "Seoul"
            ]
cities_3 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
            "SanFrancisco", "Seoul", "Rome", "Paris",
            "Jeju", "NewYork", "Rome"
            ]
cities_4 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
            "SanFrancisco", "Seoul", "Rome", "Paris",
            "Jeju", "NewYork", "Rome"
            ]
cities_5 = ["Jeju", "Pangyo", "NewYork", "newyork"]
cities_6 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

print(solution(cacheSize_1, cities_1))
print(solution(cacheSize_2, cities_2))
print(solution(cacheSize_3, cities_3))
print(solution(cacheSize_4, cities_4))
print(solution(cacheSize_5, cities_5))
print(solution(cacheSize_6, cities_6))

from collections import  deque

def solution_other(cacheSize, cities):
    answer = 0
    buffer = deque()

    # cacheSize가 0인 경우에는 참조하는 값이 없으므로 전부 5를 곱함
    if cacheSize == 0:
        return len(cities) * 5

    # 그렇지 않은경우에는, 모든 city에 대해서 확인
    # 1. city가 buffer에 있으면 +1, 그렇지 않으면 +5
    # 2. city가 buffer에 있으면 삭제하고 가장 먼저 참조된 값으로 변경 `buffer.remove(i) -> buffer.append(i)`
    # city가 buffer에 없으면, buffer의 크기와 cacheSize의 크기를 비교
    # cacheSize 보다 크기가 크면 가장 오래전 참조된 값을 삭제 `buffer.popleft()`
    # cacheSize 보다 작으면, 단순 삽입 `buffer.append(i)`
    else:
        for i in cities:
            # 대소문자는 구분하지 않으므로 lower으로 변경
            i = i.lower()
            if i in buffer:
                answer += 1
            else:
                answer += 5

            if i in buffer:
                buffer.remove(i)
            else:
                if len(buffer) >= cacheSize:
                    buffer.popleft()

            buffer.append(i)
    return answer

print(solution_other(cacheSize_1, cities_1))
print(solution_other(cacheSize_2, cities_2))
print(solution_other(cacheSize_3, cities_3))
print(solution_other(cacheSize_4, cities_4))
print(solution_other(cacheSize_5, cities_5))
print(solution_other(cacheSize_6, cities_6))

def solution_good(cacheSize, cities):
    answer = 0
    buffer = deque()

    if cacheSize == 0:
        return 5 * len(cities)

    for city in cities:
        city = city.lower()
        if city not in buffer:
            if len(buffer) == cacheSize:
                buffer.popleft()
            buffer.append(city)
            answer += 5
        else:
            buffer.remove(city)
            buffer.append(city)
            answer += 1

    return answer

print(solution_good(cacheSize_1, cities_1))
print(solution_good(cacheSize_2, cities_2))
print(solution_good(cacheSize_3, cities_3))
print(solution_good(cacheSize_4, cities_4))
print(solution_good(cacheSize_5, cities_5))
print(solution_good(cacheSize_6, cities_6))