vtx = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adj = [[1, 2],
       [0, 3],
       [0, 3, 4],
       [1, 2, 5],
       [1, 6, 7],
       [3],
       [4, 7],
       [4, 6]]

def rDFS(visited, u):
    visited[u] = True
    print(vtx[u], end=' ')

    for v in adj[u]:
        if visited[v] is False:
            rDFS(visited, v)

if __name__ == '__main__':
    visited = [False] * len(vtx)
    print('rDFS(A) : ', end='')
    rDFS(visited, 0)    # 'A'를 방문
