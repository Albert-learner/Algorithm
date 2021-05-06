# 10. 2016년

def solution(a, b):
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    answer = ''

    # 총 일수 더하는 변수
    total_day = 0

    if a > 1:
        for i in range(1, a):
            if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
                total_day += 31
            elif i == 4 or i == 6 or i == 9 or i == 11:
                total_day += 30
            elif i == 2:
                total_day += 29
        total_day += b
    else:
        total_day += b

    if total_day % 7 == 0:
        answer = day[0]
    elif total_day % 7 == 1:
        answer = day[1]
    elif total_day % 7 == 2:
        answer = day[2]
    elif total_day % 7 == 3:
        answer = day[3]
    elif total_day % 7 == 4:
        answer = day[4]
    elif total_day % 7 == 5:
        answer = day[5]
    else:
        answer = day[6]

    return answer

a_1, b_1 = 5, 24
print(solution(a_1, b_1))

def solution_best(a, b):
    answer = ''

    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    answer = days[(sum(months[:a - 1]) + b - 1) % 7]
    return answer

print(solution_best(a_1, b_1))

import datetime

def solution_other(a, b):
    answer = ''

    t = 'MON TUE WED THU FRI SAT SUN'.split()
    answer = t[datetime.datetime(2016, a, b).weekday()]
    return answer

print(solution_other(a_1, b_1))