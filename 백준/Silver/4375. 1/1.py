import sys

input = sys.stdin.readline

while 1:
  try:
    n = int(input())
  except:
    break
  i, num = 1, 0

  while 1:
    num = num*10+1
    num %= n
    if num == 0:
      print(i)
      break
    i += 1
    