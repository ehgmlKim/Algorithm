import sys
input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())
node = [[] for _ in range(n+1)]

for _ in range(m):
  i,j = map(int, input().split())
  node[i].append(j)
  node[j].append(i)
#print(node)
#방문할 수 있는 정점이 여러 개인 경우 작은 것을 먼저 방문하도록 오름차순으로 정렬
node = [sorted(x) for x in node]

def DFS(v, node, visited):
  visited[v] = 1
  print(v, end=' ')
  for x in node[v]:
    if not visited[x]:
      DFS(x, node, visited)
def BFS(v, node, visited):
  q = deque([v])
  visited[v] = 1
  while q:
    x = q.popleft()
    print(x, end=' ')
    for i in node[x]:
      if not visited[i]:
        q.append(i)
        visited[i] = 1
visited = [0]*(n+1)
DFS(v, node, visited)
print()
visited = [0]*(n+1)
BFS(v, node, visited)