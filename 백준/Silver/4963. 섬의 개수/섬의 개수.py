import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
  q = deque()
  q.append((x,y))
  visited[x][y] = True

  dx = [-1, 0, 1, 0, 1, 1, -1, -1]
  dy = [0, -1, 0, 1, -1, 1, 1, -1]

  while q:
    x, y = q.popleft()
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < h and 0 <= ny < w:
        if not visited[nx][ny] and island[nx][ny] == 1: 
          q.append((nx, ny))
          visited[nx][ny] = True

while True:
  w,h = map(int, input().split())
  answer = 0
  if w==0 and h==0:
    break
  island = list(list(map(int, input().split())) for _ in range(h))
  visited=[]
  for i in range(h):
    visited.append([False for x in range(w)])
  

  for i in range(h):
    for j in range(w):
      if island[i][j]==1 and visited[i][j] == False:
        bfs(i,j)
        answer += 1

  print(answer)