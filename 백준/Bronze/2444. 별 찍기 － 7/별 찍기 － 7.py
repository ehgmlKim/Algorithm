n = int(input())
for i in range(1, 2*n-1, 2):
  j = (2*n-1-i)//2
  print(' '*j+'*'*i)
for i in range(2*n-1, 0, -2):
  j = (2*n-1-i)//2
  print(' '*j+'*'*i)