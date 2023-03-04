import sys
input = sys.stdin.readline
t = int(input())
arr = [[0,0] for i in range(40)]
arr[0] = [1,0]
arr[1] = [0,1]
def fibo(x, arr):
  if arr[x-1] == [0,0]:
    arr[x-1] = fibo(x-1, arr)
  if arr[x-2] == [0,0]:
    arr[x-2] = fibo(x-2, arr)
  return [a+b for a,b in zip(arr[x-1],arr[x-2])]
    
for _ in range(t):
  x=int(input())
  if x==1 or x==0:
    print(arr[x][0], arr[x][1])
  else:
    ans = fibo(x, arr)
    print(ans[0], ans[1])
