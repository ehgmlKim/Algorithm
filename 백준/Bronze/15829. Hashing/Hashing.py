arr = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
L = input()
M = 1234567891
sum = 0
for i in range(n):
  a = arr.find(L[i])
  r = 31**i
  sum += (a+1)*r

print(sum%M)  