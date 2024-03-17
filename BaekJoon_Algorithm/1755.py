# 1755. 숫자 놀이

"""
I solve this problem by myself. But I need to see Other's solution for making code efficient.
See it again.
"""
# 1. My Solution
M, N = map(int, input().split())

num_to_str = {'1': "one", '2': "two", '3': "three", '4': "four",
              '5': "five", '6': "six", '7': "seven", '8': "eight",
              '9': 'nine', '0': "zero"}
str_to_int = {"one": '1', "two": '2', "three": '3', "four": '4',
              "five": '5', "six": '6', "seven": '7', "eight": '8',
              "nine": '9', "zero": '0'}

numbers_str = []
for num in range(M, N + 1):
    convert_str = ""
    num_str = str(num)
    if len(num_str) >= 2:
        for chr_idx, num_chr in enumerate(num_str):
            if chr_idx != len(num_str) - 1:
                convert_str += num_to_str[num_chr]
                convert_str += ' '
            else:
                convert_str += num_to_str[num_chr]

        numbers_str.append(convert_str)
    else:
        numbers_str.append(num_to_str[num_str])

sort_numbers = sorted(numbers_str)
answer = []
for s_num in sort_numbers:
    numbers_str = "".join(str_to_int[s_num_chr] for s_num_chr in s_num.split())
    answer.append(int(numbers_str))

for num_idx, number in enumerate(answer, 1):
    if num_idx % 10 == 0:
        print(number)
    else:
        print(number, end=' ')

# 2. Not my Solution
d = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five',
     '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}
M, N = map(int, input().split())
li = []
for i in range(M, N+1):
    s = ' '.join([d[c] for c in str(i)])
    li.append([i, s])
li.sort(key=lambda x:x[1])
for i in range(len(li)):
    if i % 10 == 0 and i != 0:
        print()
    print(li[i][0], end=' ')

"""
8 28
=>
8 9 18 15 14 19 11 17 16 13
12 10 28 25 24 21 27 26 23 22
20
"""