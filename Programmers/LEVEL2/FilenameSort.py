# 50. 파일명 정렬

def solution(files):
    answer = []

    divide_files = []
    for file_idx, file in enumerate(files):
        head = ''
        number = ''
        tail = ''
        file_idx += 1
        for ch in file:
            if not ch.isdigit():
                if len(number) == 0:
                    head += ch
                else:
                    tail += ch
            else:
                if 0 <= len(number) <= 5:
                    if len(tail) != 0:
                        tail += ch
                    else:
                        number += ch
                else:
                    tail += ch
        divide_files.append([head, number, tail])

    '''
    정렬을 하는 부분 ... 해결 못함
    '''
    divide_files = sorted(divide_files, key = lambda x : (x[0].lower(), int(x[1])))
    answer = [''.join(file) for file in divide_files]
    return answer

files_1 = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
files_2 = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
files_3 = ["foo010bar020.zip"]

# print(solution(files_1))
# print(solution(files_2))
# print(solution(files_3))

'''
내 풀이보다는 더 좋은 풀이
정규식으로 중간에 숫자값 찾고 그걸 기준으로 문자열을 나눈다
-------------------------------------------------------------
3번째 경우에는 적용이 안 되는데... 왜 이게 답이 되는 건지??
'''
import re
def solution_other(files):
    a = sorted(files, key = lambda file : int(re.findall('\d+', file)[0]))
    answer = sorted(a, key = lambda file : re.split('\d+', file.lower())[0])

    return answer

print(solution_other(files_1))
print(solution_other(files_2))
print(solution_other(files_3))

'''
1. head/number/tail을 구분한다. 숫자를 반영해서 정렬해야 하므로, 
   숫자 기준으로 split하면 된다. 정규식으로 숫자만 잘라낸 방법은 아래와 같다.
2. 숫자 기준으로 split하면 문제에서 제공한 조건에 맞게 정렬한다. 문자열
    대소문자 구분을 할 필요가 없으므로 문자열은 정렬 기준에서 통일하고,
    문자열로 되어 있는 숫자를 숫자 값에 맞춰 정렬한다.
3. 정렬된 리스트 안에 있는 split된 리스트값을 문자열로 바꿔서 출력
-------------------------------------------------------------
3번째 경우에는 적용이 안 되는데... 왜 이게 답이 되는 건지??
'''
import re
def solution_best(files):
    answer = []

    divide_files = [re.split(r'([0-9]+)', file) for file in files]
    sort = sorted(divide_files, key = lambda x: (x[0].lower(), int(x[1])))

    answer = [''.join(s) for s in sort]
    return answer

# print(solution_best(files_1))
# print(solution_best(files_2))
# print(solution_best(files_3))