n = int(input())
m = int(input())
arr = []
for i in range(n, m+1):
  cnt = 0
  if i != 1:
    for j in range(2, int(i**(1/2))+1):
      if i%j==0: 
        cnt = 1
        break
    if not cnt:
      arr += [i]
if len(arr):
    print(sum(arr))
    print(arr[0])
else:
    print(-1)