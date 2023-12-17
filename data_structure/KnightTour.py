def knight(r, c, start_x, start_y):
    board = [[-1 for _ in range(c)] for _ in range(r)]

    x = [2, 1, -1, -2, -2, -1, 1, 2]
    y = [1, 2, 2, 1, -1, -2, -2, -1]

    board[start_y][start_x] = 0     # knight 시작 지점
    pos = 1      # knight 이동 순서

    # 가능한 위치인지 검사
    if solution(r, c, board, start_x, start_y, x, y, pos):
        # 루트 순서 출력
        print(1)
        for i in range(r):
            for j in range(c):
                print(board[i][j], end= '\t')
            print()
    else:   # 끝까지 탐색하지 못한 경우
        print(0)

def solution(r, c, board, now_x, now_y, x, y, pos):
    if pos == r * c:
        return True

    # 가능한 x,y 조합 8가지 모두 탐색
    for i in range(8):
        new_x = now_x + x[i]
        new_y = now_y + y[i]
        if 0 <= new_x < c and 0 <= new_y < r and board[new_y][new_x] == -1:
            board[new_y][new_x] = pos   # 순서 집어 넣기
            if solution(r, c, board, new_x, new_y, x, y, pos+1):
                return True

            # 길을 찾을 수 없다면 Backtracking
            board[new_y][new_x] = -1
    return False

# knight(6, 8, start_x=3, start_y=2)

board = [[-1 for _ in range(8)] for _ in range(6)]
board[3][4] = 0
for i in range(6):
    for j in range(8):
        print(board[i][j], end='\t')
    print()