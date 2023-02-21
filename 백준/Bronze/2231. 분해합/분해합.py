num = int(input())

for i in range(num):
  result = sum(int(x) for x in str(i))
  result += i
  if result == num:
    print(i)
    break
else:
  print(0)