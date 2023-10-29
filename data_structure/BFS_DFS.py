# 리스트 이용
myGraph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['A', 'H'],
    'E': ['B', 'I'],
    'F': ['C', 'J'],
    'G': ['C'],
    'H': ['D'],
    'I': ['E'],
    'J': ['F']
}

def bfs_list(graph, root):
    visited = list()
    queue = list()
    queue.append(root)

    while queue:
        node = queue.pop(0)      # 앞에서부터 꺼내기
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    print('bfs : ', visited)

def dfs_list(graph, root):
    visited = list()
    stack = list()
    stack.append(root)
    while stack:
        node = stack.pop()      # 뒤에서부꺼 꺼내기
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
    print('dfs : ', visited)

bfs_list(myGraph, 'A')
dfs_list(myGraph, 'A')