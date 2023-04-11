import sys
input = sys.stdin.readline
num = input().rstrip()
l = len(num)
youjinsu = 0
for i in range(1, l):
  res1, res2 = 1,1
  a,b='', ''
  for j in range(0,i):
    a += num[j]
    res1 *= int(num[j])
  for k in range(i,l):
    b += num[k]
    res2 *= int(num[k])
  #print(a,b,res1, res2)
  if res1 == res2:
    youjinsu = 1
if youjinsu:
  print('YES')
else:
  print('NO')