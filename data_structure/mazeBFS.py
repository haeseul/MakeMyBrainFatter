from CircularQueue import CircularQueue

mat = [['1', '1', '1', '1', '1', '1'],
       ['e', '0', '0', '0', '0', '1'],
       ['1', '0', '1', '0', '1', '1'],
       ['1', '1', '1', '0', '0', 'x'],
       ['1', '1', '1', '0', '1', '1'],
       ['1', '1', '1', '1', '1', '1']]

size = 6

def isValidPos(r, c):
    if 0<=r<size and 0<=c<size:
        if mat[r][c] == '0' or mat[r][c] == 'x':
            return True
    return False

def BFS():
    q = CircularQueue()
    q.enqueue((1, 0))
    print('BFS : ')

    while not q.isEmpty():
        pos = q.dequeue()
        print(pos, end=' -> ')  # 방문
        (r, c) = pos

        if mat[r][c] == 'x':
            return True
        else:
            mat[r][c] = '.'
            if isValidPos(r-1, c): q.enqueue((r-1, c))
            if isValidPos(r+1, c): q.enqueue((r+1, c))
            if isValidPos(r, c-1): q.enqueue((r, c-1))
            if isValidPos(r, c+1): q.enqueue((r, c+1))

    return False

result = BFS()
if result: print('OK')
else: print('NO')