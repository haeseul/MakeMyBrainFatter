from ArrayStack import ArrayStack

map = [['1', '1', '1', '1', '1', '1'],
       ['e', '0', '0', '0', '0', '1'],
       ['1', '0', '1', '0', '1', '1'],
       ['1', '1', '1', '0', '0', 'x'],
       ['1', '1', '1', '0', '1', '1'],
       ['1', '1', '1', '1', '1', '1']]

size = 6


def isValidPos(r, c):
    if 0 <= r < size and 0 <= c < size:
        if map[r][c] == '0' or map[r][c] == 'x':
            return True
    return False


def DFS():
    print('DFS: ')
    s = ArrayStack(100)
    s.push((1, 0))  # 시작점

    while not s.isEmpty():
        pos = s.pop()
        print(pos, end=' -> ')
        (r, c) = pos

        if map[r][c] == 'x':
            return True
        else:
            map[r][c] = '.'

            if isValidPos(r - 1, c): s.push((r - 1, c))  # 상
            if isValidPos(r + 1, c): s.push((r + 1, c))  # 하
            if isValidPos(r, c - 1): s.push((r, c - 1))  # 좌
            if isValidPos(r, c + 1): s.push((r, c + 1))  # 우

        s.display()
    return False


result = DFS()
if result:
    print('Success')
else:
    print('Failure')
