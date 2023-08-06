import sys
import heapq
input = sys.stdin.readline
INF = 1e9
arr = []
n = int(input())
for _ in range(n):
  x = int(input())
  if x==0:
    if len(arr):
      print(heapq.heappop(arr))
    else:
      print(0)
  else:
    heapq.heappush(arr, x) 