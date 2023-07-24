import sys
from itertools import product
input = sys.stdin.readline
n, m= map(int, input().split())

arr = [x for x in range(1, n+1)]

for i in product(arr, repeat=m):
  for a in list(i):
    print(a, end=' ')
  print()