# 16. 전화번호 목록

'''문제 잘 읽어야 할 듯'''
def solution(phone_book):
    answer = True

    phone_book.sort()
    for front, rear in zip(phone_book, phone_book[1:]):
        if rear.startswith(front):
            answer = False
            return answer
    return answer

phone_book_1 = ['119', '97674223', '1195524421']
phone_book_2 = ['123', '456', '789']
phone_book_3 = ['12', '123', '1235', '567', '88']

print(solution(phone_book_1))
print(solution(phone_book_2))
print(solution(phone_book_3))

'''앞의 자리만 보는 거지, 앞 뒤로 보는 거 아님 119 97..'''
def solution_mine(phone_book):
    answer = True

    post_check = []
    for num in phone_book:
        front = int(num[0])
        rear = int(num[len(num) - 1])
        post_check.append([front, rear])

    for front, rear in zip(post_check, post_check[1:]):
        if front[len(front) - 1] == rear[0]:
            answer = False
            break

    return answer

def solution_best(phone_book):
    answer = True

    phone_book.sort()
    for front, rear in zip(phone_book, phone_book[1:]):
        if rear.startswith(front):
            answer = False
            return answer
    return answer
