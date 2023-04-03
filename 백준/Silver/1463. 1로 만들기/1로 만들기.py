import sys
input = sys.stdin.readline

n = int(input())
arr = [0 for i in range(n+1)]


for x in range(2, n+1):
  arr[x] = arr[x-1] + 1
  if x%2==0:
    arr[x] = min(arr[x//2]+1, arr[x])
  if x%3==0:
    arr[x] = min(arr[x//3]+1, arr[x])
  
print(arr[n])