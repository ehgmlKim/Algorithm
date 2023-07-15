import sys
input = sys.stdin.readline
n = int(input())

arr = sorted(list(map(int, input().split())))

m = int(input())
arr2 = list(map(int, input().split()))

def find(start, end, target):
  if start>end:
    return 0
  mid = (start+end)//2

  if target>arr[mid]:
    return find(mid+1, end, target)
  elif target<arr[mid]:
    return find(start, mid-1, target)
  else:
    return 1

for a in arr2:
  print(find(0, n-1, a), end=' ')