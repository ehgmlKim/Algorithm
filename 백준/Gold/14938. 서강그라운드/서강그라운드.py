import sys
import heapq
input = sys.stdin.readline
INF = 1e9
n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]


items = list(map(int, input().split()))
answer = 0
for _ in range(r):
  a,b,l=map(int, input().split())
  graph[a].append((b,l))
  graph[b].append((a,l))

#print(graph)

def func(start):
  q = []
  distance = [INF] * (n+1)
  heapq.heappush(q, (0, start))
  distance[start] = 0
  
  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for i in graph[now]:
      if dist+i[1] < distance[i[0]]:
        distance[i[0]] = dist+i[1]
        heapq.heappush(q, (dist+i[1], i[0]))
  #print(distance)
  sum = 0
  for i in range(1, n+1):
    if distance[i]<=m:
      sum += items[i-1]
  global answer  
  answer = max(answer, sum)

for i in range(1, n+1):
  func(i)
print(answer)