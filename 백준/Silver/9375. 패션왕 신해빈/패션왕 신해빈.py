import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
  n = int(input())
  dict = {}
  ans = 1
  for _ in range(n):
    x, y = input().split()
    if y not in dict:
      dict[y] = [x]
    else :
      dict[y].append(x)
  for d in dict.keys():
    ans *= (len(dict[d])+1)
  print(ans-1)   