class TreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def preOrder(root):
    if root:
        print('[%c] ' % root.data, end='')
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root):
    if root:
        inOrder(root.left)
        print('[%c] ' % root.data, end='')
        inOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print('[%c] ' % root.data, end='')

import queue

def levelOrder(root):
    Q = queue.Queue()
    Q.put(root)

    while not Q.empty():
        root = Q.get()
        print('[%c] ' % root.data, end='')
        if root.left:
            Q.put(root.left)
        if root.right:
            Q.put(root.right)

def leafCount(root):
    if root is None:
        return 0
    elif root.left is None and root.left is None:
        return 1
    else:
        return leafCount(root.left) + leafCount(root.right)
    # count = 0
    # if root is not None:
    #     if root.isExternal():
    #         return 1
    #     else:
    #         count = leafCount(root.left) + leafCount(root.right)
    # return count

if __name__ == '__main__':
    n6 = TreeNode('F', None, None)
    n5 = TreeNode('E', None, None)
    n4 = TreeNode('D', None, None)
    n3 = TreeNode('C', n6, None)
    n2 = TreeNode('B', n4, n5)
    n1 = TreeNode('A', n2, n3)

    print('Pre  : ', end=''); preOrder(n1); print()
    print('In   : ', end=''); inOrder(n1); print()
    print('Post : ', end=''); postOrder(n1); print()
    print('Level: ', end=''); levelOrder(n1); print()
    print(leafCount(n1))