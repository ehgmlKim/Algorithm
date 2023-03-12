import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
l = int(input())
arr = [[] for _ in range(n+1)]

#2차원 배열로 연결되어 있는 컴퓨터 표현
for _ in range(l):
  i,j = map(int, input().split())
  arr[i].append(j)
  arr[j].append(i)

def bfs(arr, start, visited):
  queue = deque([start])
  visited[start] = True
  cnt = 0
  while queue:
    v = queue.popleft()
    for i in arr[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        cnt += 1
  print(cnt)

visited = [False]*(n+1)
bfs(arr, 1, visited)