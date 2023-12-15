def dijkstra():
    weight = 0
    # 첫 원소 방문
    touch[1] = 1
    dist[1] = 0
    for e in graph[1]:
        touch[e[0]] = 1
        dist[e[0]] = e[1]

    for _ in range(n):
        min = INF
        v = 0
        for i in range(2, n+1):
            if 0 <= dist[i] < min:
                min = dist[i]
                v = i
        print('    touch = ', touch)
        print('    dist = ', dist)
        print('[%d, %d] (%2d) => %d' % (touch[v], v, dist[v], weight))
        if v not in graph:
            continue
        for e in graph[v]:
            if dist[e[0]] > dist[v]+e[1]:
                dist[e[0]] = dist[v]+e[1]
                touch[e[0]] = v

        dist[v] *= -1
        for e in graph[touch[v]]:
            if e[0] == v:
                weight += e[1]
    return weight

if __name__ == '__main__':
    for _ in range(int(input())):
        graph = {}
        for _ in range(int(input())):
            a = list(map(int, input().split()))
            i = 2
            graph[a[0]] = []
            for _ in range(a[1]):
                graph[a[0]].append((a[i], a[i + 1]))
                i += 2

        n = len(graph)
        INF = 1000
        touch = [0] * (n + 1)
        dist = [INF] * (n + 1)

        print(dijkstra())