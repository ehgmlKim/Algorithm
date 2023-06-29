n = int(input())

  
cnt = n//5
arr=[]
if n%2==0:
  arr.append(n//2)
if n%5==0:
  arr.append(n//5)
for i in range(1, cnt+1):
  n -= 5
  if n%2 == 0:
    arr.append(i + n//2)

if len(arr)>0:
    print(min(arr))
else:
    print(-1)