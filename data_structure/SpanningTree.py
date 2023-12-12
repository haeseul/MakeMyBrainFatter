vtx = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adj = [[1, 2],
       [0, 3],
       [0, 3, 4],
       [1, 2, 5],
       [2, 6, 7],
       [3],
       [4, 7],
       [4, 6]]
visited = [False] * len(vtx)

def ST(u):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            print('(%c %c)' % (vtx[u], vtx[v]), end=' ')
            ST(v)

ST(0)