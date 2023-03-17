import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
arr = [[] for i in range(n+1)]
for _ in range(m):
  u,v = map(int, input().split())
  arr[u].append(v)
  arr[v].append(u)

def bfs(arr, visited):
  cnt = 0
  for i in range(1, n+1):
    q = deque([i])
    if not visited[i]:
      cnt += 1
      while q:
        x = q.popleft()
        for i in arr[x]:
          if not visited[i]:
            q.append(i)
            visited[i] = True
  return cnt    
    
visited = [0] * (n+1)
print(bfs(arr, visited))