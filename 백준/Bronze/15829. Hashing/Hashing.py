arr = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
L = input()
str_arr = []
for l in L:
  str_arr.append(arr.find(l)+1)
M = 1234567891
result = 0
for i in range(n):
  r = 31**i
  result += (str_arr[i])*r%M
print(result)  