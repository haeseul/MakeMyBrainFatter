class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def getHeight(root):
    if root is None:
        return 0
    hLeft = getHeight(root.left)
    hRight = getHeight(root.right)

    if hLeft > hRight:
        return hLeft + 1
    else:
        return hRight + 1

def getBalance(root):
    if root is None:
        return 0
    return getHeight(root.left) - getHeight(root.right)

def rotateRight(p):     # parent
    c = p.left          # child
    p.left = c.right    # 원래 child의 오른쪽 -> parent의 left로 넘김
    c.right = p         # child의 right -> p
    return c            # 새로운 root = c

def rotateLeft(p):
    c = p.right
    p.right = c.left
    c.left = p
    return c

def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)

    balance = getBalance(root)

    # LL
    if balance > 1 and key < root.left.key:
        return rotateRight(root)
    # LR
    if balance > 1 and key > root.left.key:
        root.left = rotateLeft(root.left)
        return rotateRight(root)
    # RR
    if balance < -1 and key > root.right.key:
        return rotateLeft(root)
    # RL
    if balance < -1 and key < root.right.key:
        root.right = rotateRight(root.right)
        return rotateLeft(root)

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
    # keys = [7, 8, 9, 2, 1, 5, 3, 6, 4]
    keys = [5,3,1,7,10,8, 9]
    for key in keys:
        root = insert(root, key)
        display(root, '[Insert %2d] ' % key)