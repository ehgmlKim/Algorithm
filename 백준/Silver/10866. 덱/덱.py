import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = deque()
for _ in range(n):
  str = input().split()
  if str[0] == 'push_front':
    arr.appendleft(int(str[1]))
  elif str[0] == 'push_back':
    arr.append(int(str[1]))
  elif str[0] == 'pop_front':
    try:
      print(arr.popleft())
    except:
      print(-1)
  elif str[0] == 'pop_back':
    try:
      print(arr.pop())
    except:
      print(-1)
  elif str[0] =='size':
    print(len(arr))
  elif str[0] == 'empty':
    if len(arr):
      print(0)
    else:
      print(1)
  elif str[0] == 'front':
    if len(arr):
      print(arr[0])
    else:
      print(-1)
  else:
    if len(arr):
      print(arr[-1])
    else:
      print(-1)