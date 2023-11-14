# Restart 41. 카드 뭉치

'''
Consider the order of cards1 list and cards2 list that can make goal list.
It's important to think different when this kind of problems are coming out.
'''
def solution(cards1, cards2, goal):
    answer = 'Yes'

    for goal_str in goal:
        if cards1 and goal_str == cards1[0]:
            del cards1[0]
        elif cards2 and goal_str == cards2[0]:
            del cards2[0]
        else:
            answer = 'No'

    return answer

# Same as Previous solution but this is using list pop function. And consider conditions about list length and element is in list or not.
def solution_other(cards1, cards2, goal):
    answer = 'Yes'

    for goal_str in goal:
        if len(cards1) > 0 and goal_str == cards1[0]:
            cards1.pop(0)
        elif len(cards2) > 0 and goal_str == cards2[0]:
            cards2.pop(0)
        else:
            answer = 'No'

    return answer

cards1_1 = ["i", "drink", "water"]
cards1_2 = ["i", "water", "drink"]

cards2_1 = ["want", "to"]
cards2_2 = ["want", "to"]

goal_1 = ["i", "want", "to", "drink", "water"]
goal_2 = ["i", "want", "to", "drink", "water"]

print(solution(cards1_1, cards2_1, goal_1))
print(solution(cards1_2, cards2_2, goal_2))

cards1_1 = ["i", "drink", "water"]
cards1_2 = ["i", "water", "drink"]

cards2_1 = ["want", "to"]
cards2_2 = ["want", "to"]

goal_1 = ["i", "want", "to", "drink", "water"]
goal_2 = ["i", "want", "to", "drink", "water"]

print(solution_other(cards1_1, cards2_1, goal_1))
print(solution_other(cards1_2, cards2_2, goal_2))