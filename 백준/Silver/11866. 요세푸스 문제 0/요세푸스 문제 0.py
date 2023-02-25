n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
idx = k-1
count = 1
print("<", end='')
for _ in range(n-1):
  print(arr.pop(idx), end=", ")
  idx = idx+k-1
  if idx>=len(arr):
    idx = idx%len(arr)
print(arr[0], ">", sep="")