Graph = {'A': [('B', 29), ('F', 10)],
         'B': [('A', 29), ('C', 16), ('G', 15)],
         'C': [('B', 16), ('D', 12)],
         'D': [('C', 12), ('E', 22), ('G', 18)],
         'E': [('D', 22), ('F', 27), ('G', 25)],
         'F': [('A', 10), ('E', 27)],
         'G': [('B', 15), ('D', 18), ('E', 25)]}

n = len(Graph)
vertices = [-1] * n
eList = []

def edgeSort():
    for v in Graph:
        for e in Graph[v]:
            if v < e[0]:
                eList.append([v, e[0], e[1]])
    eList.sort(key=lambda e:e[2], reverse=True)

def find(v):
    while vertices[v] != -1:
        v = vertices[v]
    return v

def union(s1, s2):
    vertices[s2] = s1

def Kruskal():
    edge = 0
    edgeSort()

    while edge < n-1:
        # 최소 edge 선택
        e = eList.pop()
        # set 확인
        s1 = find(ord(e[0])-65)
        s2 = find(ord(e[1])-65)
        if s1 != s2:
            edge += 1
            union(s1, s2)
            print('%d. [%c%c %d] ' % (edge, e[0], e[1], e[2]))

Kruskal()
