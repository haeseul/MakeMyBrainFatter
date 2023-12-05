def dfs_iter(v, num, visited, graph):
    stack = [v]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            num[0] += 1
            stack.extend(graph[node])
    return visited

def connected(graph, size):
    visited = [False for _ in range(size+1)]
    nums = []
    for v in range(1, size+1):
        if not visited[v]:
            num = [0]
            dfs_iter(v, num, visited, graph)
            nums.append(num[0])
    return nums

if __name__ == "__main__":
    numTestCases = int(input())

    for _ in range(numTestCases):
        n = int(input())
        graph = [[] for _ in range(n+1)]
        for i in range(n):
            adjacency = list(map(int, input().split()))
            vertex = adjacency.pop(0)
            graph[vertex] = adjacency[1:]

        nums = connected(graph, vertex)
        nums = sorted(nums)
        print(len(nums), end=' ')
        for i in nums:
            print(i, end=' ')
        print()