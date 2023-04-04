import sys

input = sys.stdin.readline
num = input().rstrip()
dict = {}
for n in num:
  if n == '9':
    if '6' not in dict:
      dict['6'] = 1
    else:
      dict['6'] += 1
  else:
    if n not in dict:
      dict[n] = 1
    else:
      dict[n] += 1
dict = sorted(dict.items(), key=lambda x: (x[1], x))
#print(dict)
if dict[-1][0] == '6':
  val1 = (dict[-1][1] - 1) // 2 + 1
  if len(dict)>1:
    val2 = dict[-2][1]
    print(val1 if val1 > val2 else val2)
  else:
    print(val1)
else:
  print(dict[-1][1])
