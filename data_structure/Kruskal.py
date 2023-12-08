Graph = {'A': [('B', 29), ('F', 10)],
         'B': [('A', 29), ('C', 16), ('G', 15)],
         'C': [('B', 16), ('D', 12)],
         'D': [('C', 12), ('E', 22), ('G', 18)],
         'E': [('D', 22), ('F', 27), ('G', 25)],
         'F': [('A', 10), ('E', 27)],
         'G': [('B', 15), ('D', 18), ('E', 25)]}

vertices = [-1] * len(Graph)    # weight 로 정렬된 edges
eList = []                      # 두 vertex, edge weight

def edgeSort():
    for v in Graph:         # A, B, C, D ..
        for e in Graph[v]:  # ('B', 29), ('F', 10) ..
            if v < e[0]:    # AB
                eList.append([v, e[0], e[1]])
    eList.sort(key = lambda e : e[2], reverse=True)     # weight 기준 정렬
    for i in range(len(eList)-1, -1, -1):
        print('[%c%c%d] ' % (eList[i][0], eList[i][1], eList[i][2]), end='')
    print();print();

def find(vNum):
    while vertices[vNum] != -1:
        vNum = vertices[vNum]
    return vNum

def union(vNum1, vNum2):
    vertices[vNum2] = vNum1     # vNum2 를 vNum1의 것으로 업데이트

def kruskal():
    eCnt = 0    # edge count ( <= n-1 )
    vCnt = len(Graph)

    edgeSort()

    while eCnt < vCnt-1:                # edge count ( <= n-1 )
        e = eList.pop()                 # 최소 weight 추출 ['A', 'F', 10]
        vNum1 = find(ord(e[0])-65)      # 'A' -> 집합 0
        vNum2 = find(ord(e[1])-65)      # 'F' -> 집합 5
        if vNum1 != vNum2:
            eCnt += 1
            print('%d. [%c%c %d] ' % (eCnt, e[0], e[1], e[2]))
            union(vNum1, vNum2)

if __name__ == '__main__':
    kruskal()