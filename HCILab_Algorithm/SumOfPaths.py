# 1. 경로 노드들의 합 구하기

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def deserialize(self, new_node):
        if not self.root:
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if temp.val != 'null':
                if not temp.left:
                    temp.left = new_node
                    return
                queue.append(temp.left)
                if not temp.right:
                    temp.right = new_node
                    return
                queue.append(temp.right)

    def level_sum(self, root, val = 0, target = 0):
        cnt = 0
        val += [int(root.val) if root.val != 'null' else 0][0]

        if root.left:
            if root.left.val == 'null':
                if val == target:
                    return 1
            else:
                cnt += self.level_sum(root.left, val, target)
        else:
            if val == target:
                return 1

        if root.right and root.right.val != 'null':
            cnt += self.level_sum(root.right, val, target)
        return cnt

def solution(tree, k):
    answer = 0

    t = BinaryTree()
    for node in tree.split(','):
        t.deserialize(Node(node))

    answer = t.level_sum(t.root, target = k)
    return answer

tree_1 = '5,4,8,11,null,13,4,7,2,null,null,5,1'
tree_2 = '7,3,8,13,4,10,9,2,1,16,null,5,null,null,6'
tree_3 = '9,2,4,14,null,8,5'
tree_4 = '3,7,8,4,9,13,17,5,null,12,2,10,14,1,6'
tree_5 = '10'
tree_6 = '4,2,5,12,6,5,8,null,null,8,2,null,6,3,1'
tree_7 = '5,2,4,10,11,15,7,6,8,35,22,16,37,22,24'
tree_8 = '3,7,2,15,24,13,11'
tree_9 = '1,7,9,10,11,8,9,17,17,11,14,17,3,16,4'
tree_10 = '9,2,4,14,null,8,5'
tree_11 = '3,7,8,4,9,13,17,5,null,12,2,10,14,1,6'
tree_12 = '7,8,5,3,7,4,null,5,2,9,8,null,7,null,null'
tree_13 = '5,4,8,11,null,13,4,7,2,null,null,5,1'
tree_14 = '5,3,9,8,null,2,null'
tree_15 = '7,1,3,8,5,9,null,4,9,12,2,6,null,null,null'

k_1 = 22
k_2 = 30
k_3 = 25
k_4 = 30
k_5 = 10
k_6 = 20
k_7 = 40
k_8 = 40
k_9 = 35
k_10 = 15
k_11 = 21
k_12 = 23
k_13 = 26
k_14 = 16
k_15 = 25

print(solution(tree_1, k_1))
print(solution(tree_2, k_2))
print(solution(tree_3, k_3))
print(solution(tree_4, k_4))
print(solution(tree_5, k_5))
print()
print(solution(tree_6, k_6))
print(solution(tree_7, k_7))
print(solution(tree_8, k_8))
print(solution(tree_9, k_9))
print(solution(tree_10, k_10))
print(solution(tree_11, k_11))
print(solution(tree_12, k_12))
print(solution(tree_13, k_13))
print(solution(tree_14, k_14))
print(solution(tree_15, k_15))