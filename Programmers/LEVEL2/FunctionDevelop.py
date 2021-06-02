# 40. 기능 개발

def solution(progresses, speeds):
    answer = []

    release_day = 0
    finished_time = []
    for progress, speed in zip(progresses, speeds):
        release_day += 1
        course_rate = progress + speed * release_day
        while course_rate < 100:
            release_day += 1
            course_rate = progress + speed * release_day
        finished_time.append(release_day)
        release_day = 0

    front = 0
    for index in range(len(finished_time)):
        if finished_time[front] < finished_time[index]:
            answer.append(index - front)
            front = index
    answer.append(len(finished_time) - front)
    return answer

progresses_1 = [93, 30, 55]
progresses_2 = [95, 90, 99, 99, 80, 99]

speeds_1 = [1, 30, 5]
speeds_2 = [1, 1, 1, 1, 1, 1]

# print(solution(progresses_1, speeds_1))
# print(solution(progresses_2, speeds_2))

def solution_best(progresses, speeds):
    answer = []

    for progress, speed in zip(progresses, speeds):
        if len(answer) == 0 or answer[-1][0] < -((progress - 100) // speed):
            answer.append([-((progress - 100) // speed), 1])
        else:
            answer[-1][1] += 1

    answer = [ans[1] for ans in answer]
    return answer

print(solution_best(progresses_1, speeds_1))
print(solution_best(progresses_2, speeds_2))