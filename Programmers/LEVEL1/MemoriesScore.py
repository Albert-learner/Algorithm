# Restart 37. 추억 점수

def solution(name, yearning, photo):
    answer = []

    name_year_dict = {n : ye for n, ye in zip(name, yearning)}
    for pho in photo:
        missing_score = 0
        for person in pho:
            if person in name_year_dict.keys():
                missing_score += name_year_dict[person]

        answer.append(missing_score)
    return answer

name_1 = ["may", "kein", "kain", "radi"]
name_2 = ["kali", "mari", "don"]
name_3 = ["may", "kein", "kain", "radi"]

yearning_1 = [5, 10, 1, 3]
yearning_2 = [11, 1, 55]
yearning_3 = [5, 10, 1, 3]

photo_1 = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
photo_2 = [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]
photo_3 = [["may"],["kein", "deny", "may"], ["kon", "coni"]]

print(solution(name_1, yearning_1, photo_1))
print(solution(name_2, yearning_2, photo_2))
print(solution(name_3, yearning_3, photo_3))

