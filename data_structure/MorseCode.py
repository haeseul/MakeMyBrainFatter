table =[('A', '.-'),    ('B', '-...'),  ('C', '-.-.'),  ('D', '-..'),
        ('E', '.'),     ('F', '..-.'),  ('G', '--.'),   ('H', '....'),
        ('I', '..'),    ('J', '.---'),  ('K', '-.-'),   ('L', '.-..'),
        ('M', '--'),    ('N', '-.'),    ('O', '---'),   ('P', '.--.'),
        ('Q', '--.-'),  ('R', '.-.'),   ('S', '...'),   ('T', '-'),
        ('U', '..-'),   ('V', '...-'),  ('W', '.--'),   ('X', '-..-'),
        ('Y', '-.--'),  ('Z', '--..') ]

def encode(ch):
    idx = ord(ch) - ord('A')
    return table[idx][1]    # return code

def decodeFromTable(code):
    for e in table:
        if code == e[1]:
            return e[0]     # return alphabet
    return None

class TreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def makeMorseTree():
    root = TreeNode(None, None, None)
    for e in table:
        code = e[1]
        node = root     # 화살표 역할
        for c in code:
            if c == '.':
                if node.left is None:
                    node.left = TreeNode(None, None, None)
                node = node.left
            elif c == '-':
                if node.right is None:
                    node.right = TreeNode(None, None, None)
                node = node.right
        node.data = e[0]        # 알파벳 사용
    return root

if __name__ == '__main__':
    str = input("Input a string : ")
    encoded = []
    for ch in str:
        code = encode(ch)
        encoded.append(code)

    print('Morse Code : ', encoded)
    print('Decoding   : ', end=' ')
    for code in encoded:
        print(decodeFromTable(code), end='')

    # Morse Tree 에서 decode 하는 코드 만들기