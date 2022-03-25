# 1. 지도 자동 구축

N = int(input('점의 개수 : '))

k, total = 2, 0
for i in range(N):
    total += (2 ** i)

print((k + total) * (k + total))