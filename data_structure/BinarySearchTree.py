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