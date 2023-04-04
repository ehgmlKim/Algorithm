import sys
input = sys.stdin.readline
n = int(input())
have = list(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))

have.sort()

def func(start, end, target):
  if start>end:
    return 0
  mid = (start + end)//2
  if target == have[mid]:
    return 1
  elif target > have[mid]:
    return func(mid+1, end, target)
  else:
    return func(start, mid-1, target)
for i in num:
  print(func(0, n-1, i), end=' ')