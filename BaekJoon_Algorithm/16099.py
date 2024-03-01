# 16099. Larger Sport Facility

# 1. My Solution
Ts = int(input())
answers = []
areas_info = [list(map(int, input().split())) for _ in range(Ts)]

for tele_l, tele_w, euro_l, euro_w in areas_info:
    tele_area, euro_area = tele_l * tele_w, euro_l * euro_w
    if tele_area < euro_area:
        answers.append("Eurocom")
    elif tele_area > euro_area:
        answers.append("TelecomParisTech")
    else:
        answers.append("Tie")

for answer in answers:
    print(answer)

# 2. Not my Solution
Ts = int(input())
results = []

for _ in range(Ts):
    tele_l, tele_w, euro_l, euro_w = map(int, input().split())
    tele_area, euro_area = tele_l * tele_w, euro_l * euro_w

    if tele_area < euro_area:
        results.append("Eurecom")
    elif tele_area > euro_area:
        results.append("TelecomParisTech")
    else:
        results.append("Tie")

# Print the results
for result in results:
    print(result)

"""
2
3 2 4 2
536874368 268792221 598 1204
=>
Eurecom
TelecomParisTech
"""