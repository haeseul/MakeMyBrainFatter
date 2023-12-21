from queue import LifoQueue, Queue

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

def iDFS(u):
    S = LifoQueue()
    S.put(u)
    visited[u] = True
    print(vtx[u], end=' ')

    while not S.empty():
        u = S.get()
        S.put(u)
        flag = True
        for v in adj[u]:
            if not visited[v]:
                S.put(v)
                visited[v] = True
                print(vtx[v], end=' ')
                flag = False
                break
        if flag:
            S.get()
iDFS(0)