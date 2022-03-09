# 29. 광고 삽입

def str_to_seconds(time):
    h, m, s = time.split(':')

    return int(h) * 3600 + int(m) * 60 + int(s)

def seconds_to_str(time):
    h = str(time // 3600).zfill(2)
    time %= 3600
    m = str(time // 60).zfill(2)
    s = str(time % 60).zfill(2)

    return ':'.join([h, m, s])

def solution(play_time, adv_time, logs):
    answer = ''

    play_time = str_to_seconds(play_time)
    adv_time = str_to_seconds(adv_time)
    all_time = [0 for i in range(play_time + 1)]

    for log in logs:
        start, end = log.split('-')
        start = str_to_seconds(start)
        end = str_to_seconds(end)
        all_time[start] += 1
        all_time[end] -= 1

    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    most_view = 0
    max_time = 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1

    answer += seconds_to_str(max_time)
    return answer

play_time_1 = "02:03:55"
play_time_2 = "99:59:59"
play_time_3 = "50:00:00"

adv_time_1 = "00:14:15"
adv_time_2 = "25:00:00"
adv_time_3 = "50:00:00"

logs_1 = ["01:20:15-01:45:14",
          "00:40:31-01:00:00",
          "00:25:50-00:48:29",
          "01:30:59-01:53:29",
          "01:37:44-02:02:30"]
logs_2 = ["69:59:59-89:59:59",
          "01:00:00-21:00:00",
          "79:59:59-99:59:59",
          "11:00:00-31:00:00"]
logs_3 = ["15:36:51-38:21:49",
          "10:14:18-15:36:51",
          "38:21:49-42:51:45"]

print(solution(play_time_1, adv_time_1, logs_1))
print(solution(play_time_2, adv_time_2, logs_2))
print(solution(play_time_3, adv_time_3, logs_3))

'''
다른 풀이
'''
def solution_other(play_time, adv_time, logs):
    answer = ''

    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    all_time = [0 for i in range(play_time + 1)]

    for log in logs:
        start, end = log.split('-')
        start = str_to_int(start)
        end = str_to_int(end)
        all_time[start] += 1
        all_time[end] -= 1

    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    most_view = 0
    max_time = 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1

    answer += int_to_str(max_time)
    return answer

def str_to_int(time):
    h, m, s = time.split(':')

    return int(h) * 3600 + int(m) * 60 + int(s)

def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time %= 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time %= 60
    s = '0' + str(time) if time < 10 else str(time)

    return h + ':' + m + ':' + s

# print(solution_other(play_time_1, adv_time_1, logs_1))
# print(solution_other(play_time_2, adv_time_2, logs_2))
# print(solution_other(play_time_3, adv_time_3, logs_3))

'''
zfill함수(0으로 채우기)
str.zfill(n) : str의 길이가 n보다 작으면 길이가 n이 되도록 앞에 '0'을 채움.
'''
def to_seconds(time):
    h, m, s = map(int, time.split(':'))

    return h * 3600 + m * 60 + s

def to_time(time):
    h = str(time // 3600).zfill(2)
    time %= 3600
    m = str(time // 60).zfill(2)
    s = str(time % 60).zfill(2)

    return ':'.join([h, m, s])

def solution_best(play_time, adv_time, logs):
    answer = ''

    play_time = to_seconds(play_time)
    adv_time = to_seconds(adv_time)

    memo = [0 for _ in range(play_time + 1)]

    for log in logs:
        start, end = map(str, log.split('-'))
        start = to_seconds(start)
        end = to_seconds(end)

        memo[start] += 1
        memo[end] += -1

    for i in range(1, play_time + 1):
        memo[i] = memo[i] + memo[i - 1]

    for i in range(1, play_time + 1):
        memo[i] = memo[i] + memo[i - 1]

    max_play = memo[adv_time - 1]
    start = 0

    for i in range(adv_time, play_time):
        play = memo[i] - memo[i - adv_time]

        if play > max_play:
            max_play = play
            start = i - adv_time + 1

    answer = to_time(start)
    return answer

# print(solution_best(play_time_1, adv_time_1, logs_1))
# print(solution_best(play_time_2, adv_time_2, logs_2))
# print(solution_best(play_time_3, adv_time_3, logs_3))