import sys
n, m =map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
tree.sort()
def binary(start, end, m):
  mid = (start+end) // 2
  h = [t-mid for t in tree if t>mid]
  if (start>end):
    print(end)
    return end
  if sum(h) >= m:
    binary(mid+1, end, m)
  else:
    binary(start, mid-1, m)
    
binary(1, tree[-1], m)