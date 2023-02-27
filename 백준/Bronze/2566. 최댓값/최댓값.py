arr = []
now = []
x, y = 0, 0
max_v = -1
for i in range(9):
  now = list(map(int, input().split()))
  for j in range(9):
    if now[j]>max_v:
      max_v = now[j]
      x = i
      y = j
  arr.append(now)
print(max_v)
print(x+1, y+1)