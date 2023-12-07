Graph = {'A': [('B', 29), ('F', 10)],
         'B': [('A', 29), ('C', 16), ('G', 15)],
         'C': [('B', 16), ('D', 12)],
         'D': [('C', 12), ('E', 22), ('G', 18)],
         'E': [('D', 22), ('F', 27), ('G', 25)],
         'F': [('A', 10), ('E', 27)],
         'G': [('B', 15), ('D', 18), ('E', 25)]}

INF = 100
dist = [INF] * len(Graph)
visited = [False] * len(Graph)

def findMin():
    minDist = INF
    minV = 0

    for v in range(len(dist)):
        if visited[v] == False and dist[v] < minDist:
            minDist = dist[v]
            minV = v

    return minV

def prim(v):
    vCnt = len(Graph)
    dist[ord(v)-65] = 0         # 아스키코드

    for i in range(vCnt):
        # for j in range(vCnt):
        #     print('%3d ' % dist[j], end='')
        print()
        vNum = findMin()
        v = chr(vNum + 65)      # 다시 문자로 변경

        visited[vNum] = True
        print('[%c (%d)] ' % (v, dist[vNum]), end='')

        for e in Graph[v]:
            vNum = ord(e[0])-65
            if visited[vNum] == False and e[1] < dist[vNum]:
                # 방문한 적 없고 가중치가 dist보다 작으면 업데이트
                dist[vNum] = e[1]

if __name__ == '__main__':
    prim('C')       # 시작 정점 지정