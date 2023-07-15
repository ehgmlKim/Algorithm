import sys
input = sys.stdin.readline
n, k = map(int, input().split())

arr = [i for i in range(1, n+1)]
answer = []
idx = 0
while len(arr)>0:
  idx = (idx + k -1)%len(arr)
  x = arr.pop(idx%len(arr))
  answer.append(x)
print("<", end="")
for i in range(len(answer)):
  if i==len(answer)-1:
    print(answer[i], end='')
  else:
    print(answer[i], end=', ')
print(">")