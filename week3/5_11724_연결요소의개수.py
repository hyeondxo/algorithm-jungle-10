import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(n+1)]
total_count = 0


def dfs(node):
    visited[node] = True
    for next in graph[node]:
        if not visited[next]:
            dfs(next)


for node in range(1, n+1):
    if not visited[node]:
        dfs(node)
        total_count += 1

print(total_count)
