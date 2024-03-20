# 2161. 카드1

"""
I solve this problem by myself. See again for using Python collection's deque.
The positive value of deque's rotate function means rotate sequence in a right way.
Negative means rotate sequence in a left way.
"""
# 1. My Solution
from collections import deque

N = int(input())
cards = deque([num for num in range(1, N + 1)])
discards = []

while len(cards) >= 1:
    discards.append(cards.popleft())
    cards.rotate(-1)

print(*discards)

# 2. Not my Solution



"""
7
=>
1 3 5 7 4 2 6

"""