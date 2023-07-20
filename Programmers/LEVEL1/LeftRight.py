# Restart 31. 왼쪽 오른쪽

'''
Error
There's not any mention about if 'l' or 'r' in str_list.
Then follow the same rule that was mentioned at previous state.
'''
def solution(str_list):
    answer = []

    for i in range(len(str_list)):
        if str_list[i] == 'l':
            answer = str_list[:i]
            return answer
        elif str_list[i] == 'r':
            answer = str_list[i + 1:]
            return answer

    return answer

str_list_1 = ["u", "u", "l", "r"]
str_list_2 = ["l"]

print(solution(str_list_1))
print(solution(str_list_2))

'''
I didn't consider if 'l' and 'r' in str_list
'''
def solution_wrong(str_list):
    answer = str_list[:str_list.index('l')] if 'l' in str_list else str_list[str_list.index('r') + 1:] if 'r' in str_list else []

    return answer