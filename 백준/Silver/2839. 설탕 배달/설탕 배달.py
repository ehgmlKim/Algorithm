n = int(input())
answer = []
if n%3==0:
  answer.append(n//3)
if n%5==0:
  answer.append(n//5)

i = 0
while n>0:
  n -= 3
  i += 1
  if n%5==0:
    i += n//5
    answer.append(i)
    break

if len(answer):
  print(min(answer))
else:
  print(-1)