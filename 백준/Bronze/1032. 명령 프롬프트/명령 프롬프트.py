import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
  arr.append(input())
idx = set()
l = len(arr[0])
for i in range(1, n):
  x = arr[i]
  for j in range(l):
    if arr[0][j] != x[j]:
      idx.add(j)
for i in range(l):
  if i in idx:
    print('?', end='')
  else:
    print(arr[0][i], end='')