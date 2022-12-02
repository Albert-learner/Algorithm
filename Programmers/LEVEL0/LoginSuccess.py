# Restart 15. 로그인 성공?

# My Wrong Solution
'''
조건문 만으로 처리할 수 없음
id와 password 모두 다 고려하는 조건이어야 하기 때문에
'''
def solution_wrong(id_pw, db):
    answer = 'login' if id_pw[0] in [data[0] for data in db] and id_pw[1] in [data[1] for data in db] \
    else 'wrong pw' if id_pw[0] in [data[0] for data in db] and id_pw[1] not in [data[1] for data in db] else 'fail'

    return answer

id_pw_1 = ["meosseugi", "1234"]
id_pw_2 = ["programmer01", "15789"]
id_pw_3 = ["rabbit04", "98761"]

db_1 = [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]
db_2 = [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]
db_3 = [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]

# print(solution_wrong(id_pw_1, db_1))
# print(solution_wrong(id_pw_2, db_2))
# print(solution_wrong(id_pw_3, db_3))

# Use for loop
def solution(id_pw, db):
    answer = 'fail'

    for data in db:
        if id_pw[0] in data:
            if id_pw[1] == data[1]:
                answer = 'login'
            else:
                answer = 'wrong pw'
    return answer

print(solution(id_pw_1, db_1))
print(solution(id_pw_2, db_2))
print(solution(id_pw_3, db_3))

# Use Hash
def solution_best(id_pw, db):
    answer = 'fail'
    db_dict = {data[0] : data[1] for data in db}

    if id_pw[0] in db_dict:
        if id_pw[1] == db_dict[id_pw[0]]:
            answer = 'login'
        else:
            answer = 'wrong pw'
    return answer

print(solution_best(id_pw_1, db_1))
print(solution_best(id_pw_2, db_2))
print(solution_best(id_pw_3, db_3))