a=int(input())
b=int(input())
c=int(input())

result = a*b*c
dict={}
for k in range(0, 10):
  dict[str(k)] = 0
for i in str(result):
  dict[i] += 1
for v in dict.values():
  print(v)

