from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (m+1)]
graph += [[0] + list(map(int, list(input().strip()))) for _ in range(n)]

def bfs(a, b):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    q = deque([(a, b)])
    graph[a][b] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 1 <= nx <= n and 1 <= ny <= m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return graph[n][m]
print(bfs(1, 1)+1)