# 16. 단어 변환

# BFS를 이용한 풀
def solution(begin, target, words):
    answer = 0

    change_lst = [begin]
    if target not in words:
        answer = 0
    else:
        while len(words) != 0:
            for item in change_lst:
                possible_words = []
                for word in words:
                    check = 0
                    for one in range(len(item)):
                        if item[one] != word[one]:
                            check += 1
                        if check == 2:
                            break

                    if check == 1:
                        possible_words.append(word)
                        words.remove(word)
            answer += 1
            if target in possible_words:
                return answer
            else:
                change_lst = possible_words
    return answer

begin_1 = 'hit'
begin_2 = 'hit'

target_1 = 'cog'
target_2 = 'cog'

words_1 = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
words_2 = ['hot', 'dot', 'dog', 'lot', 'log']

print(solution(begin_1, target_1, words_1))
print(solution(begin_2, target_2, words_2))

def BFS(begin, target, words, visited):
    count = 0
    stack = [(begin, 0)]

    while stack:
        cur, depth = stack.pop()
        if cur == target:
            return depth

        for i in range(len(words)):
            if visited[i] == True:
                continue
            cnt = 0
            for a, b in zip(cur, words[i]):
                if a != b:
                    cnt += 1
            if cnt == 1:
                visited[i] = True
                stack.append((words[i], depth + 1))

def solution_bfs(begin, target, words):
    answer = 0

    if target not in words:
        return answer

    visited = [False] * len(words)

    answer = BFS(begin, target, words, visited)
    return answer

begin_1 = 'hit'
begin_2 = 'hit'

target_1 = 'cog'
target_2 = 'cog'

words_1 = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
words_2 = ['hot', 'dot', 'dog', 'lot', 'log']

# print(solution_bfs(begin_1, target_1, words_1))
# print(solution_bfs(begin_2, target_2, words_2))

def DFS(current, word):
    match_count = 0
    for c, w in zip(current, word):
        if c == w:
            match_count += 1

    if match_count == len(word) - 1:
        return True
    else:
        return False

def solution_dfs(begin, target, words):
    if target not in words:
        return 0

    answer = 0
    visited = [0] * len(words)
    current_lst = [begin]

    while current_lst:
        current = current_lst.pop()
        if current == target:
            return answer

        for i in range(len(words)):
            if not visited[i]:
                if DFS(current, words[i]):
                    visited[i] = 1
                    current_lst.append(words[i])
        answer += 1
    return answer

begin_1 = 'hit'
begin_2 = 'hit'

target_1 = 'cog'
target_2 = 'cog'

words_1 = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
words_2 = ['hot', 'dot', 'dog', 'lot', 'log']

# print(solution_dfs(begin_1, target_1, words_1))
# print(solution_dfs(begin_2, target_2, words_2))

