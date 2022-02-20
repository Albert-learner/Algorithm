# 27. 길 찾기 게임

import sys
sys.setrecursionlimit(10 ** 6)

def preorder(arrY, arrX, answer):
    node = arrY[0]
    idx = arrX.index(node)
    arrY1, arrY2 = [], []

    for i in range(1, len(arrY)):
        if node[0] > arrY[i][0]:
            arrY1.append(arrY[i])
        else:
            arrY2.append(arrY[i])

    answer.append(node[2])
    if len(arrY1) > 0:
        preorder(arrY1, arrX[:idx], answer)
    if len(arrY2) > 0:
        preorder(arrY2, arrX[idx + 1:], answer)

    return

def postorder(arrY, arrX, answer):
    node = arrY[0]
    idx = arrX.index(node)
    arrY1, arrY2 = [], []

    for i in range(1, len(arrY)):
        if node[0] > arrY[i][0]:
            arrY1.append(arrY[i])
        else:
            arrY2.append(arrY[i])

    if len(arrY1) > 0:
        postorder(arrY1, arrX[:idx], answer)
    if len(arrY2) > 0:
        postorder(arrY2, arrX[idx + 1:], answer)
    answer.append(node[2])

    return

def solution(nodeinfo):
    answer = []
    preanswer, postanswer = [], []

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)

    arrY = sorted(nodeinfo, key = lambda x : (-x[1], x[0]))
    arrX = sorted(nodeinfo)

    preorder(arrY, arrX, preanswer)
    postorder(arrY, arrX, postanswer)

    answer = [preanswer, postanswer]
    return answer

nodeinfo_1 = [[5, 3],
              [11, 5],
              [13, 3],
              [3, 5],
              [6, 1],
              [1, 3],
              [8, 6],
              [7, 2],
              [2, 2]
              ]

print(solution(nodeinfo_1))

class Tree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

preorderList = []
postorderList = []

def preorder_1(node, nodeinfo):
    preorderList.append(nodeinfo.index(node.data) + 1)
    if node.left:
        preorder_1(node.left, nodeinfo)
    if node.right:
        preorder_1(node.right, nodeinfo)

def postorder_1(node, nodeinfo):
    if node.left:
        postorder_1(node.left, nodeinfo)
    if node.right:
        postorder_1(node.right, nodeinfo)
    postorderList.append(nodeinfo.index(node.data) + 1)

def solution_other(nodeinfo):
    answer = []

    sortedNodeinfo = sorted(nodeinfo, key = lambda x : (-x[1], x[0]))

    root = None
    for node in sortedNodeinfo:
        if not root:
            root = Tree(node)
        else:
            current = root
            while True:
                if node[0] < current.data[0]:
                    if current.left:
                        current = current.left
                        continue
                    else:
                        current.left = Tree(node)
                if node[0] > current.data[0]:
                    if current.right:
                        current = current.right
                        continue
                    else:
                        current.right = Tree(node)
                        break
                break

    preorder_1(root, nodeinfo)
    postorder_1(root, nodeinfo)
    answer.append(preorderList)
    answer.append(postorderList)
    return answer

print(solution_other(nodeinfo_1))