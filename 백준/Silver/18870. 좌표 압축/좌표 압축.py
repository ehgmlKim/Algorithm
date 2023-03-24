import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
set_arr = sorted(list(set(arr)))
dict = {}
for i,v in enumerate(set_arr):
  dict[v] = i
for a in arr:
  print(dict[a], end=' ')