n = int(input())
arr= []
answer = []
for _ in range(n):
  x,y = map(int, input().split())
  arr.append((x,y))
for x,y in arr:
  count = 0
  for a,b in arr:
    if x < a and y < b:
      count += 1
  answer.append(count)
for a in answer:
  print(a+1, end=' ')