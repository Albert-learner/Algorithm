# Restart 43. 개인정보 수집 유효기간

'''
This is Kakao Blind Recruitment problem.
I can rewind using Python's datetime library. This problem calculate month, so 28days for one month doens't matter.
See this again for studying datetime library. This is the best solution I think.
'''
from datetime import datetime
from dateutil.relativedelta import relativedelta
def solution(today, terms, privacies):
    answer = []

    today = datetime.strptime(today, "%Y.%m.%d")
    today = today.strftime("%Y.%m.%d")
    terms_dict = {term.split()[0] : int(term.split()[1]) for term in terms}
    end_dates_lst = []
    for privacy in privacies:
        start_date, p_term = privacy.split()
        start_date = datetime.strptime(start_date, "%Y.%m.%d")
        add_month = terms_dict[p_term]

        end_date = start_date + relativedelta(months = add_month)
        end_date = end_date.strftime("%Y.%m.%d")
        end_dates_lst.append(end_date)

    # print(end_dates_lst)
    for dt_idx in range(1, len(end_dates_lst) + 1):
        if today >= end_dates_lst[dt_idx - 1]:
            answer.append(dt_idx)

    return answer

'''
Compare today and calculated privacy date and terms
'''
# If valid, True
def date_comparison(expiration_date, today):
    # Compare year
    if expiration_date[0] > today[0]:
        return True

    # Compare Month
    if expiration_date[0] == today[0] and expiration_date[1] > today[1]:
        return True

    # Compare Day
    if expiration_date[0] == today[0] and expiration_date[1] == today[1] and expiration_date[2] > today[2]:
        return True

    return False

def solution_other(today, terms, privacies):
    answer = []

    idx = 1
    today = list(map(int, today.split('.')))
    expiration = {term[0] : int(term[2:]) for term in terms}

    for privacy in privacies:
        privacy = privacy.split()
        privacy_date = list(map(int, privacy[0].split(".")))
        privacy_date[1] += expiration[privacy[1]]

        # If month is over 12
        if privacy_date[1] > 12:
            if privacy_date[1] % 12 == 0:
                privacy_date[0] += (privacy_date[1] // 12) - 1
                privacy_date[1] = 12
            else:
                privacy_date[0] += privacy_date[1] // 12
                privacy_date[1] %= 12

        if date_comparison(privacy_date, today) == False:
            answer.append(idx)

        idx += 1
    return answer

'''
Calculate all times with small unit(in here day)
This is easy for understanding.
'''
def to_days(date):
    year, month, day = map(int, date.split('.'))
    return year * 28 * 12 + month * 28 + day

def solution_other_easy(today, terms, privacies):
    answer  = []

    month_to_days = {term[0] : int(term[2:]) * 28 for term in terms}
    today = to_days(today)
    answer = [
        pri_idx for pri_idx, privacy in enumerate(privacies, 1)
        if to_days(privacy[:-2]) + month_to_days[privacy[-1]] <= today
    ]
    return answer

today_1 = "2022.05.19"
today_2 = "2020.01.01"

terms_1 = ["A 6", "B 12", "C 3"]
terms_2 = ["Z 3", "D 5"]

privacies_1 = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
privacies_2 = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

print(solution(today_1, terms_1, privacies_1))
print(solution(today_2, terms_2, privacies_2))

print(solution_other(today_1, terms_1, privacies_1))
print(solution_other(today_2, terms_2, privacies_2))

print(solution_other_easy(today_1, terms_1, privacies_1))
print(solution_other_easy(today_2, terms_2, privacies_2))
