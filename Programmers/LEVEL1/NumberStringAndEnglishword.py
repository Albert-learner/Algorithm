# 47. 숫자 문자열과 영단어

def solution(s):
    answer = 0

    digit_to_num_dict = {'zero' : 0, 'one' : 1,
                         'two' : 2, 'three' : 3,
                         'four' : 4, 'five' : 5,
                         'six' : 6, 'seven' : 7,
                         'eight' : 8, 'nine' : 9
                         }

    answer_str = ''
    num_str = ''
    for ch in s:
        if ch.isalpha():
            num_str += ch
            if num_str in digit_to_num_dict.keys():
                answer_str += str(digit_to_num_dict[num_str])
                num_str = ''
        else:
            answer_str += ch
    answer = int(answer_str)

    return answer

s_1 = "one4seveneight"
s_2 = "23four5six7"
s_3 = "2three45sixseven"
s_4 = "123"

# print(solution(s_1))
# print(solution(s_2))
# print(solution(s_3))
# print(solution(s_4))

def solution_best(s):
    answer = s
    num_dict = {'zero' : '0', 'one' : '1',
                'two' : '2', 'three' : '3',
                'four' : '4', 'five' : '5',
                'six' : '6', 'seven' : '7',
                'eight' : '8', 'nine' : '9'}

    for key, value in num_dict.items():
        answer = answer.replace(key, value)

    answer = int(answer)
    return answer

print(solution_best(s_1))
print(solution_best(s_2))
print(solution_best(s_3))
print(solution_best(s_4))