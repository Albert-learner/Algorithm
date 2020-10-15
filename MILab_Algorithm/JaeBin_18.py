# 18. 프로그래머스 - 셔틀버스

def solution(n, t, m, timetable):
    answer = ''

    minute_timetable = [int(time[:2]) * 60 + int(time[3:5]) for time in timetable]
    # print('Minute_timetable before sort : ', minute_timetable)

    # 분 단위로 통일해서 정렬
    minute_timetable.sort()
    # print('Minute_timetable after sort : ', minute_timetable)

    last_time = (60 * 9) + (n - 1) * t
    # print('Last time that Con`s aboard : ', last_time)

    for step in range(n):
        if len(minute_timetable) < m:
            answer = '%02d:%02d' % (last_time // 60, last_time % 60)
            return answer

        if step == n - 1:
            if minute_timetable[0] <= last_time:
                last_time = minute_timetable[m-1] - 1
            answer = '%02d:%02d' % (last_time // 60, last_time % 60)
            return answer

        for i in range(m-1, -1, -1):
            bus_arrive = (60 * 9) + step * t
            if minute_timetable[i] <= bus_arrive:
                del minute_timetable[i]


n_1 = 1
t_1 = 1
m_1 = 5
timetable_1 = ['08:00', '08:01', '08:02', '08:03']

n_2 = 2
t_2 = 10
m_2 = 2
timetable_2 = ['09:10', '09:09', '08:00']

n_3 = 2
t_3 = 1
m_3 = 2
timetable_3 = ['00:01', '00:01', '00:01', '00:01', '00:01']

n_4 = 1
t_4 = 1
m_4 = 1
timetable_4 = ['23:59']

n_5 = 10
t_5 = 60
m_5 = 45
timetable_5 = ['23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59',
               '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59',
               '23:59', '23:59']

# print(solution(n_1, t_1, m_1, timetable_1))
# print()
print(solution(n_2, t_2, m_2, timetable_2))
print()
# print(solution(n_3, t_3, m_3, timetable_3))
# print()
# print(solution(n_4, t_4, m_4, timetable_4))
# print()
# print(solution(n_5, t_5, m_5, timetable_5))
