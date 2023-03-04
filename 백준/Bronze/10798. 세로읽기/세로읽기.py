import sys
input = sys.stdin.readline
arr = []
str = ''
for _ in range(5):
  arr.append(list(input().rstrip()))
i = 0
for j in range(15):
  for i in range(5):
    if len(arr[i]):
      x = arr[i].pop(0)
      str += x
print(str)