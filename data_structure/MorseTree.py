table =[('A', '.-'),    ('B', '-...'),  ('C', '-.-.'),  ('D', '-..'),
        ('E', '.'),     ('F', '..-.'),  ('G', '--.'),   ('H', '....'),
        ('I', '..'),    ('J', '.---'),  ('K', '-.-'),   ('L', '.-..'),
        ('M', '--'),    ('N', '-.'),    ('O', '---'),   ('P', '.--.'),
        ('Q', '--.-'),  ('R', '.-.'),   ('S', '...'),   ('T', '-'),
        ('U', '..-'),   ('V', '...-'),  ('W', '.--'),   ('X', '-..-'),
        ('Y', '-.--'),  ('Z', '--..') ]

# ch -> code
def encode(ch):
    idx = ord(ch) - ord('A')
    return table[idx][1]

# morse -> ch
def decode(code):
    for i in table:
        if code == i[1]:
            return i[0]
    return None

class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def MorseTree():
    root = TreeNode()
    for e in table:
        code = e[1]
        node = root     # node pointer
        for c in code:
            if c == '.':
                if node.left is None:
                    node.left = TreeNode()
                node = node.left
            elif c == '-':
                if node.right is None:
                    node.right = TreeNode()
                node = node.right
        node.data = e[0]
    return root

def decodeFromTree(root, code):
    node = root
    for c in code:
        if c == '.':
            node = node.left
        elif c == '-':
            node = node.right
    return node.data

str = input('String: ')
encoded = []
for ch in str:
    code = encode(ch)
    encoded.append(code)

print('Morse Code : ', encoded)

print('Decoding   : ', end=' ')
for code in encoded:
    print(decode(code), end='')
print()

root = MorseTree()
print('Decoding form Tree : ', end=' ')
for code in encoded:
    print(decodeFromTree(root, code), end='')