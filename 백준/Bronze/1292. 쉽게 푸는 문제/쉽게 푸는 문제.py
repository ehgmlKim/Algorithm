import sys

input = sys.stdin.readline
A, B = map(int, input().split())
arr = []
count = 1
start = 1
while count<B+1:
  for i in range(start):
    arr.append(start)
    count += 1
  start += 1
#print(arr)
sum = 0
for i in range(A, B+1):
  sum += arr[i-1]
print(sum)