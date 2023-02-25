import sys
n = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
for b in B:
  if b > A[n-1] or b < A[0]:
    print(0)
  else:
    if b in A:
      print(1)
    else:
      print(0)