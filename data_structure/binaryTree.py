class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, value=None):
        self.root = Node(value)

    def insert(self, value):
        if self.root.value is None:
            self.root.value = value
            return
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert_recursive(node.right, value)

    def size(self, node):
        if node is None: return 0
        return 1 + self.size(node.left) + self.size(node.right)

    def height(self, node):
        if node is None: return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def sumOfWeight(self, node):
        if node is None: return 0
        return node.value + self.sumOfWeight(node.left) + self.sumOfWeight(node.right)

    def maxPathWeight(self, node):
        if node is None: return 0
        return node.value + max(self.maxPathWeight(node.left), self.maxPathWeight(node.right))

    def mirror(self, node):
        if node is None: return
        tmp = node.left
        node.left = node.right
        node.right = tmp
        self.mirror(node.left)
        self.mirror(node.right)

    def preOrder(self, node):
        if node:
            print(node.value, end=' ')
            self.preOrder(node.left)
            self.preOrder(node.right)

    def inOrder(self, node):
        if node:
            self.inOrder(node.left)
            print(node.value, end=' ')
            self.inOrder(node.right)

    def postOrder(self, node):
        if node:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.value, end=' ')

    def destruct(self):
        self.destruct_recursive(self.root)
        self.root = None

    def destruct_recursive(self, node):
        if node is None: return
        self.destruct_recursive(node.left)
        self.destruct_recursive(node.right)
        del node


if __name__ == '__main__':
    # 출력순서: size, height, sumOfWeight, maxPathWeight, (mirror), pre, in, post, destruct
    numTestCases = int(input())

    for _ in range(numTestCases):
        tree = BinaryTree()

        a = list(map(int, input().split()))
        num = a.pop(0)
        for i in range(num):
            tree.insert(a[i])

        print(tree.size(tree.root))
        print(tree.height(tree.root))
        print(tree.sumOfWeight(tree.root))
        print(tree.maxPathWeight(tree.root))
        tree.mirror(tree.root)
        tree.preOrder(tree.root)
        print()
        tree.inOrder(tree.root)
        print()
        tree.postOrder(tree.root)
        tree.destruct()
        print()
        if tree.root is None: print(0)
        else: print(1)