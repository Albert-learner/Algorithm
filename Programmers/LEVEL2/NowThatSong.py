# 49. 방금그곡

# '#'을 변환해주는 함수
def change_sharp(sheet):
    sheet = sheet.replace('C#', 'c')
    sheet = sheet.replace('D#', 'd')
    sheet = sheet.replace('F#', 'f')
    sheet = sheet.replace('G#', 'g')
    sheet = sheet.replace('A#', 'a')

    return sheet

def caltime(musicinfo):
    start_time = musicinfo[0]
    end_time = musicinfo[1]
    hour = 1 * (int(end_time.split(':')[0]) - int(start_time.split(':')[0]))
    if hour == 0:
        total_time = int(end_time.split(':')[1]) - int(start_time.split(':')[1])
    else:
        total_time = 60 * hour + int(end_time.split(':')[1]) - int(start_time.split(':')[1])

    return total_time

def solution(m, musicinfos):
    answer = []

    m = change_sharp(m)
    for idx, music_info in enumerate(musicinfos):
        music_info = change_sharp(music_info)
        music_info = music_info.split(',')
        playing_time = caltime(music_info)

        if len(music_info[3]) >= playing_time:
            melody = music_info[3][:playing_time]
        else:
            q, r = divmod(playing_time, len(music_info[3]))
            melody = music_info[3] * q + music_info[3][:r]

        if m in melody:
            answer.append([idx, playing_time, music_info[2]])

    if len(answer) != 0:
        answer = sorted(answer, key = lambda x: (-x[1], x[0]))
        return answer[0][2]

    return '(None)'

m_1 = "ABCDEFG"
m_2 = "CC#BCC#BCC#BCC#B"
m_3 = "ABC"

musicinfos_1 = ["12:00,12:14,HELLO,CDEFGAB",
                "13:00,13:05,WORLD,ABCDEF"]
musicinfos_2 = ["03:00,03:30,FOO,CC#B",
                "04:00,04:08,BAR,CC#BCC#BCC#B"]
musicinfos_3 = ["12:00,12:14,HELLO,C#DEFGAB",
                "13:00,13:05,WORLD,ABCDEF"]

print(solution(m_1, musicinfos_1))
print(solution(m_2, musicinfos_2))
print(solution(m_3, musicinfos_3))

'''
내 풀이(datetime 모듈을 이용해서 풀어보기)
'#' 문자 바꾸는 과정 필요함
마지막에 (None)을 return해야 함.
해결함
'''

def change(sheet):
    sheet = sheet.replace('A#', 'a')
    sheet = sheet.replace('C#', 'c')
    sheet = sheet.replace('D#', 'd')
    sheet = sheet.replace('F#', 'f')
    sheet = sheet.replace('G#', 'g')


    return sheet

from datetime import datetime
def solution_mine(m, musicinfos):
    answer = ''

    m = change(m)
    timeformat = '%H:%M'
    real_sheet_music_lst = []
    for idx, music_info in enumerate(musicinfos):
        music = music_info.split(',')
        start_time, end_time = datetime.strptime(music[0], timeformat), \
                               datetime.strptime(music[1], timeformat)
        playing_time = int((end_time - start_time).seconds / 60)
        music_name = music[2]
        sheet_music = change(music[3])

        if len(sheet_music) < playing_time:
            q, r = divmod(playing_time, len(sheet_music))
            real_sheet_music = sheet_music * q + sheet_music[:r]
        else:
            real_sheet_music = sheet_music[:playing_time]

        if m in real_sheet_music:
            real_sheet_music_lst.append([idx, playing_time, music_name])

    if len(real_sheet_music_lst) != 0:
        real_sheet_music_lst = sorted(real_sheet_music_lst, key=lambda x: (-x[1], x[0]))
        answer = real_sheet_music_lst[0][2]
        return answer

    if len(answer) == 0:
        answer = '(None)'

    return answer

# print(solution_mine(m_1, musicinfos_1))
# print(solution_mine(m_2, musicinfos_2))
# print(solution_mine(m_3, musicinfos_3))

'''
다른 사람 풀이
거의 똑같음.
'''
def change_signature(music):
    if 'A#' in music:
        music = music.replace('A#', 'a')
    if 'F#' in music:
        music = music.replace('F#', 'f')
    if 'C#' in music:
        music = music.replace('C#', 'c')
    if 'G#' in music:
        music = music.replace('G#', 'g')
    if 'D#' in music:
        music = music.replace('D#', 'd')

    return music

def solution_other(m, musicinfos):
    answer = []
    index = 0  # 먼저 입력된 음악을 판단하기 위해 index 추가
    for info in musicinfos:
        index += 1
        music = info.split(',')
        start = music[0].split(':')  # 시작 시간
        end = music[1].split(':')  # 종료 시간
        # 재생시간 계산
        time = (int(end[0]) * 60 + int(end[1])) - (int(start[0]) * 60 + int(start[1]))

        # 악보에 #이 붙은 음을 소문자로 변환
        changed = change(music[3])

        # 음악 길이
        a = len(changed)

        # 재생시간에 재생된 음
        b = changed * (time // a) + changed[:time % a]

        # 기억한 멜로디도 #을 제거
        m = change(m)

        # 기억한 멜로디가 재생된 음에 있다면 결과배열에 [시간, index, 제목]을 추가
        if m in b:
            answer.append([time, index, music[2]])

    # 결과배열이 비어있다면 "None" 리턴
    if not answer:
        return "(None)"
    # 결과배열의 크기가 1이라면 제목 리턴
    elif len(answer) == 1:
        return answer[0][2]
    # 결과 배열의 크기가 2보다 크다면 재생된 시간이 긴 음악, 먼저 입력된 음악순으로 정렬
    else:
        answer = sorted(answer, key=lambda x: (-x[0], x[1]))
        return answer[0][2]  # 첫번째 제목을 리턴

# print(solution_other(m_1, musicinfos_1))
# print(solution_other(m_2, musicinfos_2))
# print(solution_other(m_3, musicinfos_3))