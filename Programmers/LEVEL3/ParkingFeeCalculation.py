# 32. 주차 요금 계산

import math
def TimeToMinutes(time):
    hours, minutes = map(int, time.split(':'))

    return hours * 60 + minutes

def solution(fees, records):
    answer = []

    default_time, default_fee, unint_time, unit_fee = fees

    record_dict = dict()
    for record in records:
        time, car_number, history = record.split()
        car_number = int(car_number)
        if car_number in record_dict:
            record_dict[car_number].append([TimeToMinutes(time), history])
        else:
            record_dict[car_number] = [[TimeToMinutes(time), history]]

    request_lst = list(record_dict.items())
    request_lst.sort(key=lambda x: x[0])


    for request in request_lst:
        total_time = 0

        for case in request[1]:
            if case[1] == 'IN':
                total_time -= case[0]
            else:
                total_time += case[0]

        if request[1][-1][1] == 'IN':
            total_time += TimeToMinutes('23:59')

        if total_time <= default_time:
            answer.append(default_fee)
        else:
            answer.append(default_fee + math.ceil((total_time - default_time) / unint_time) * unit_fee)
    return answer

fees_1 = [180, 5000, 10, 600]
fees_2 = [120, 0, 60, 591]
fees_3 = [1, 461, 1, 10]

records_1 = ["05:34 5961 IN",
             "06:00 0000 IN",
             "06:34 0000 OUT",
             "07:59 5961 OUT",
             "07:59 0148 IN",
             "18:59 0000 IN",
             "19:09 0148 OUT",
             "22:59 5961 IN",
             "23:00 5961 OUT"]
records_2 = ["16:00 3961 IN",
             "16:00 0202 IN",
             "18:00 3961 OUT",
             "18:00 0202 OUT",
             "23:58 3961 IN"]
records_3 = ["00:00 1234 IN"]

print(solution(fees_1, records_1))
print(solution(fees_2, records_2))
print(solution(fees_3, records_3))

from collections import defaultdict
from math import ceil

class Parking:
    def __init__(self, fees):
        self.fees = fees
        self.in_flag = False
        self.in_time = 0
        self.total = 0

    def update(self, t, inout):
        self.in_flag = True if inout == 'IN' else False
        if self.in_flag:
            self.in_time = str2int(t)
        else:
            self.total += (str2int(t)-self.in_time)

    def calc_fee(self):
        if self.in_flag: self.update('23:59', 'out')
        add_t = self.total - self.fees[0]
        return self.fees[1] + ceil(add_t/self.fees[2]) * self.fees[3] if add_t >= 0 else self.fees[1]

def str2int(string):
    return int(string[:2])*60 + int(string[3:])

def solution_other(fees, records):
    recordsDict = defaultdict(lambda:Parking(fees))
    for rcd in records:
        t, car, inout = rcd.split()
        recordsDict[car].update(t, inout)
    return [v.calc_fee() for k, v in sorted(recordsDict.items())]

print(solution_other(fees_1, records_1))
print(solution_other(fees_2, records_2))
print(solution_other(fees_3, records_3))