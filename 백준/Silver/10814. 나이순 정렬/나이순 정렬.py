import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
  x,y = input().split()
  arr.append([i,x,y])


arr = sorted(arr, key = lambda x : (int(x[1]), x[0]))

for i, x, y in arr:
  print(x, y)