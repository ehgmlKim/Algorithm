import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()
m = int(input())
arr = list(map(int, input().split()))

def find(start, end, target):
  if start>end:
    return 0

  mid = (start + end)//2

  if A[mid] > target:
    return find(start, mid-1, target)
  elif A[mid] < target:
    return find(mid+1, end, target)
  else:
    return 1

for a in arr:
  print(find(0,n-1,a))