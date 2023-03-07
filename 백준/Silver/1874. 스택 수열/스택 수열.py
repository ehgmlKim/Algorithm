import sys
input = sys.stdin.readline
n = int(input())
arr = []
num = []
for _ in range(n):
  arr.append(int(input()))

i = 1
answer = []
while len(arr) and len(num)<=n:
  if not len(num) : #아무것도 안들어있으면
    num.append(i)
    answer.append('+')
    i += 1
  else:
    if num[-1] == arr[0]:
      answer.append('-')
      num.pop(-1)
      arr.pop(0)
    else:
      answer.append('+')
      num.append(i)
      i += 1

if not len(num):
  for a in answer:
    print(a)
else:
  print('NO')