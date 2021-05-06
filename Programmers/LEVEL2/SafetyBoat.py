# 17. 구명보트

def solution(people, limit):
    answer = 0
    people.sort()

    i, j = 0, len(people) - 1
    while i <= j:
        answer += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return answer

people_1 = [70, 50, 80, 50]
people_2 = [70, 80, 50]

limit_1 = 100
limit_2 = 100

print(solution(people_1, limit_1))
print(solution(people_2, limit_2))