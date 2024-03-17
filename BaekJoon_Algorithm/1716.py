# 1716. Polynomial Remains

"""
I didn't solve this problem by myself. I didn't catch the key point of this problem(Because of English Explanation).
First point is that the end condition of this problem.
And last is that the meaning of remains at Polynomial coefficients.
"""
# 1. My Solution
while True:
    N, K = map(int, input().split())
    if N == -1 and K == -1:
        break

    coefficients = list(map(int, input().split()))
    for i in range(N, K - 1, -1):
        coefficients[i - K] -= coefficients[i]
        coefficients[i] = 0

    rests = []
    for i in range(N, -1, -1):
        if coefficients[i]:
            rests.append(coefficients[i])

    if not rests:
        rests.append(0)

    print(*rests[::-1])

# 2. Not my Solution(ChatGPT)
while True:
    n, k = map(int, input().split())
    if n == -1 and k == -1:
        break

    coefs_lst = list(map(int, input().split()))
    for i in range(n, k - 1, -1):
        coefs_lst[i - k] -= coefs_lst[i]
        coefs_lst[i] = 0

    st = []
    for i in range(n, -1, -1):
        if coefs_lst[i]:
            st.append(coefs_lst[i])

    if not st:
        st.append(0)

    print(*st[::-1])
"""
5 2
6 3 3 2 0 1
5 2
0 0 3 2 0 1
4 1
1 4 1 1 1
6 3
2 3 -3 4 1 0 1
1 0
5 1
0 0
7
3 5
1 2 3 4
-1 -1
=>
3 2
-3 -1
-2
-1 2 -3
0
0
1 2 3 4
"""