# 1. 설탕 배달

'''C++과 같은 풀이인데 무슨 오류인지 모르겠네... 백준에서 오류남(내 풀이)
    입력 받을 때 숫자만 입력받아야하고, -1을 문자열로 출력해야 함'''
N = int(input())
bag = 0

while True:
    if N % 5 == 0:
        print(N // 5 + bag)
        break
    elif N <= 0:
        print('-1')
        break
    N -= 3
    bag += 1

'''남의 풀이'''
sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)