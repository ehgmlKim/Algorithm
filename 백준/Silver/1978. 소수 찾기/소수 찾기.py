n = int(input())
arr =list(map(int, input().split()))

answer = 0
for a in arr:
  count = 0
  for i in range(2, a):
    if a%i==0:
      n -= 1
      break
  if a==1:
    n -= 1
print(n)