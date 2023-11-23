class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert_recur(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = insert_recur(root.left, key)
    elif key > root.key:
        root.right = insert_recur(root.right, key)
    return root

def min_key_node(root):
    while root is not None and root.left is not None:
        root = root.left
    return root

def max_key_node(root):
    while root is not None and root.right is not None:
        root = root.right
    return root

def deleteNode(root, key):
    if root is None:
        return None
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:   # 삭제할 key를 찾은 경우
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            succ = min_key_node(root.right)
            root.key = succ.key
            root.right = deleteNode(root.right, succ.key)
    return root

def in_order(root):
    if root:
        in_order(root.left)
        print('%2d ' % root.key, end='')
        in_order(root.right)

def display(root, msg):
    print(msg, end='')
    in_order(root)
    print()

if __name__ == '__main__':
    root = None
    keys = [35, 18, 7, 26, 3, 22, 30, 12, 26, 68, 99]

    for key in keys:
        root = insert_recur(root, key)
        display(root, '[Insert %2d] ' % key)

    print('\nmax key : %d' % max_key_node(root).key)
    print('min key : %d' % min_key_node(root).key)

    # root = deleteNode(root, 30)
    # display(root, '[Delete 30:] ')
    # root = deleteNode(root, 26)
    # display(root, '[Delete 26:] ')
    root = deleteNode(root, 18)
    display(root, '[Delete 18:] ')
