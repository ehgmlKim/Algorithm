import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
  str = input().split()
  if str[0] == 'push':
    arr.append(int(str[1]))
  elif str[0] == 'pop':
    try:
      print(arr.pop(-1))
    except:
      print(-1)
  elif str[0] =='size':
    print(len(arr))
  elif str[0] == 'empty':
    if len(arr):
      print(0)
    else:
      print(1)
  else:
    if len(arr):
      print(arr[-1])
    else:
      print(-1)