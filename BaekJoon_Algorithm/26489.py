# 26489. Gum Gum for Jay Jay

"""
I almost solve this problem by myself. But I don't know how to solve RunTimeError.
The key of this problem is using try except.
"""
# 1. My Solution
answers = 0
while True:
    try:
        line = input()
        if line == "gum gum for jay jay":
            answers += 1
    except EOFError:
        break

print(answers)

# 2. Not my Solution
def gum_gum_for_jay_jay():
    answer = 0

    while True:
        try:
            gum_gum = input()
            answer += 1
        except EOFError:
            break

    return answer


if __name__ == "__main__":
    print(gum_gum_for_jay_jay())


"""
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
=>
11
"""