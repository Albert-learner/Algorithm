# Restart 17. 치킨 쿠폰

'''
Not my solution, key point is coupons operation.
'''
def solution(chicken):
    answer = 0
    coupons = chicken
    while coupons >= 10:
        service = coupons // 10
        answer += service
        coupons = coupons % 10 + service
    return answer

chicken_1 = 100
chicken_2 = 1081

print(solution(chicken_1))
print(solution(chicken_2))

'''
Almost same, but I have to consider coupon rest
'''
def solution_mine(chicken):
    answer = 0

    coupons = 0
    while chicken >= 10:
        if chicken != 10:
            service, coupon = divmod(chicken, 10)
            answer += service
            coupons += coupon
            if coupons >= 10:
                coup_service, coup_coupon = divmod(coupons, 10)
                answer += coup_service
                coupons = coup_coupon
        else:
            service, coupon = 1, 1
            answer += service
            coupons += coupon
        chicken //= 10

    return answer

print(solution_mine(chicken_1))
print(solution_mine(chicken_2))