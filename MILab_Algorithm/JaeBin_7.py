# 6. RGB 거리 2

house_count = int(input())
house_architecture = []
min_sum = 0

for t in range(house_count):
    Red, Green, Blue = map(int, input().split())
    house_info = [Red, Green, Blue]
    house_architecture.append(house_info)


