dict = {}
while True:
  n=int(input())
  cnt = 0
  if n == 0:
    break
  for i in range(n+1, 2*n+1):
    if i in dict:
      if dict[i]:
        cnt += 1
    else: 
      dict[i] = True
      for j in range(2, int(i**0.5)+1):
        if i%j==0:
          dict[i] = False
          break
      if dict[i]:
        cnt += 1
  print(cnt)
        