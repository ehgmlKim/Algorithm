n = int(input())
arr = []
for _ in range(n):
  str = input()
  if str not in arr:
    arr.append(str)
arr.sort(key = lambda x : (len(x), x))

for a in arr:
  print(a)