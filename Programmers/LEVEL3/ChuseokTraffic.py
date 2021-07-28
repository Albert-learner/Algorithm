# 1. 추석 트래픽

'''
초당 최대 처리량 : 어떤 특정 초 사이(에를 들면 2 ~ 3초 사이)에 처리량이 가장 많을 때의 값
처리시간은 시작시간과 끝시간 포함, 밀리세컨드까지 나오기 때문에 값을 다 초로 바꾸고 X 1000
'''
# 초당 최대 처리량
def check_traffic(time, li):
    c = 0
    start = time
    end = time + 1000

    for i in li:
        if i[1] >= start and i[0] < end:
            c += 1

    return c


def solution(lines):
    answer = 1

    lst = []

    for line in lines:
        day, end_time, dispose_time = line.split()
        end_time = end_time.split(':')
        dispose_time = float(dispose_time.replace('s', '')) * 1000
        end = (int(end_time[0]) * 3600 + int(end_time[1]) * 60 + float(end_time[2])) * 1000
        start = end - dispose_time + 1
        lst.append([start, end])

    for i in lst:
        answer = max(answer, check_traffic(i[0], lst), check_traffic(i[1], lst))

    return answer

lines_1 = [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]
lines_2 = [
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]
lines_3 = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

print(solution(lines_1))
print(solution(lines_2))
print(solution(lines_3))

def get_times(log):
    log_str = log.split()
    end_time = log_str[1].split(':')
    end_time = int(end_time[0]) * 3600000 + int(end_time[1]) * 60000 + \
                int(end_time[2].replace('.', ''))
    start_time = end_time - int(float(log_str[2].replace('s', '')) * 1000) + 1

    return (start_time, end_time) if start_time > 0 else (0, end_time)

def solution_other(lines):
    answer = 0
    total_times = []
    for i in range(len(lines)):
        start_time, end_time = get_times(lines[i])
        total_times.append((start_time, end_time, i))

    for i in range(len(total_times)):
        count = 1
        end_time = total_times[i][1]
        for j in range(len(total_times)):
            if i == j:
                continue
            t_start_time = total_times[j][0]
            t_end_time = total_times[j][1]
            if t_start_time >= end_time and t_start_time < end_time + 1000:
                count += 1
            elif t_end_time >= end_time and t_end_time < end_time + 1000:
                count += 1
            elif end_time >= t_start_time and end_time + 1000 <= t_end_time:
                count += 1

        if count > answer:
            answer = count

    return answer

# print(solution_other(lines_1))
# print(solution_other(lines_2))
# print(solution_other(lines_3))

'''
시간 계산에 있어서 유용한 datetime 모듈 이용하여 풀기
'''
from datetime import datetime
def solution_best(lines):
    answer = 0

    range_list = []
    pointer_list = []

    for line in lines:
        # ex) "2016-09-15 01:00:04.001 2.0s",
        # dt = 2016-09-15 01:00:04.001
        # dr = 2.0s
        dt = line.split()[0] + ' ' + line.split()[1]
        dr = line.split()[2]

        # strptime을 통한 dt 형식 변환 : 문자열(기존) >> 날짜(변경)
        dt = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f')

        # dr[:-1]을 통해 맨 뒤 문자열 "s" 제거,
        # float()함수를 통해 타입 변경 : 문자열(기존) >> 실수(변경)
        # * 1000을 통해 단위 변경 : 초(기존) >> 밀리초(변경)
        # int()를 통해서 타입 변경 : 실수(기존) >> 정수(변경)
        # ex) dr = 2.0s(기존) >> 2000(변경)
        dr = int(float(dr[:-1]) * 1000)

        # line의 dt는 처리가 끝난 시각이 기록되어있고, 끝난 시각을 밀리초로 환산하여 end 변수에 할당.
        # 1. hour, minute, second를 각각 단위에 맞게 계산하여 초로 변환 후 * 1000 = millisecond로 변환
        # 2. microsecond를 구하고 //1000을 통해서 millisecond를 구해서 더해줌
        end = (dt.second + dt.minute * 60 + dt.hour * 3600) * 1000 + dt.microsecond // 1000

        # end = dt = 처리가 끝난 시각
        # start = 처리가 끝난 시각 - 걸린 시각 + 1 = 처리 시작 시각
        # ex) 2016-09-15 03:10:33.020 0.011s
        # "2016년 9월 15일 오전 3시 10분 33.010초"부터
        # "2016년 9월 15일 오전 3시 10분 33.020초"까지 "0.011초"
        start = end - dr + 1

        # pointer_list에 start, end 포인트를 각각 넣어주고,
        # range_list에는 start, end를 묶은 범위 tuple을 넣어줌.
        pointer_list.append(start)
        pointer_list.append(end)
        range_list.append((start, end))

        # 여기서부터 잘 생각해야하는게,
        # 문제에서 원하는 답은 최대 처리량을 갖는 "1초" 구간임.
        # 최대 값은 start나 end 포인트를 기점으로 나옴.
        # why? 그 외에 범위에서는 변화가 없기 때문.

        # 따라서, start, end 포인트를 시작으로 1초 즉, point + 999 의 범위 내에
        # range_list에 넣은 놈들이 포함되냐 안되냐를 count하고 그 max 값을 찾으면 됨.

    # pointer_list를 돌면서 각 pointer로부터 +999의 범위 내에 range_list의 놈들이 포함되려면,
    # 아래 첨부한 사진을 참조해서
    # 1. range의 end가 point보다 작거나(앞이거나)
    # 2. range의 start가 point+999보다 크거나(뒤거나)
    # 위의 두 경우는 우리가 구하고 싶은 범위에 포함되지 않으니 "넘어가고"
    # 그 경우들을 제외한 나머지 경우에 대해서 count+1을 해줄거다.

    # 이 내용이 바로 아래 for 문 중에
    # if not(range_item[1] < pointer) and not(range_item[0] > pointer + 999):
    #     count += 1

    # 각 변수 세팅
    max_count = 0
    count = 0

    for pointer in pointer_list:
        count = 0
        # pointer_list를 돌면서 start 혹은 end 포인트를 꺼내오고
        # 새 pointer를 가져올 때, count = 0 초기화
        for range_item in range_list:
            if not (range_item[1] < pointer) and not (range_item[0] > pointer + 999):
                count += 1

                # 각 pointer와 range를 돌면서 새로운 최고값이 나오면 max_count를 갱신
                if count > max_count:
                    max_count = count

    answer = max_count
    return answer

# print(solution_best(lines_1))
# print(solution_best(lines_2))
# print(solution_best(lines_3))