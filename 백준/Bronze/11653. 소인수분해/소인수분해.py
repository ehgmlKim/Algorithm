n = int(input())
arr = []
while n>1:
  for i in range(2, n+1):
    if n%i==0:
      arr += [i]
      n //= i
      break
if len(arr):
  for a in arr:
    print(a)