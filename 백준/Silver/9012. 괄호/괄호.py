t = int(input())
for _ in range(t):
  str = input()
  arr = []
  check = True
  for s in str:
    if s == '(':
      arr.append(s)
    else:
      if len(arr):
        arr.pop()
      else:
        check = False
  if not len(arr) and check:
    print('YES')
  else:
    print('NO')