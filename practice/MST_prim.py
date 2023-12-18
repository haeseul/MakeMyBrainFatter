Graph = {'A': [('B', 29), ('F', 10)],
         'B': [('A', 29), ('C', 16), ('G', 15)],
         'C': [('B', 16), ('D', 12)],
         'D': [('C', 12), ('E', 22), ('G', 18)],
         'E': [('D', 22), ('F', 27), ('G', 25)],
         'F': [('A', 10), ('E', 27)],
         'G': [('B', 15), ('D', 18), ('E', 25)]}

INF = 100
n = len(Graph)
visited = [0] * n
dist = [INF] * n

def findMin():
    min = INF
    minV = 0
    for v in range(n):
        if not visited[v] and dist[v] < min:
            min = dist[v]
            minV = v
    return minV

def prim(v):    # v = chr
    # 시작 정점
    dist[ord(v)-65] = 0

    for i in range(n):
        # 선택된 정점과 가장 가까운 정점 선택
        minV = findMin()
        visited[minV] = 1
        v = chr(minV+65)
        print('[%c (%2d)] ' % (v, dist[minV]), end='')

        for e in Graph[v]:
            v2 = ord(e[0])-65
            if not visited[v2] and dist[v2] > e[1]:
                dist[v2] = e[1]
        print()

prim('C')