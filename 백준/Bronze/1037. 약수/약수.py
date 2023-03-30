import sys

input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
if n==1:
  print(arr[0]**2)
else:
  print(arr[0]*arr[-1])