import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
  arr.append(input())
#문자가 다른 인덱스를 담는 집합
idx = set()
l = len(arr[0]) #문자열 길이
for i in range(1, n):
  x = arr[i]
  for j in range(l):
    if arr[0][j] != x[j]: #첫번째 문자와 다르면 해당 문자의 인덱스를 추가한다
      idx.add(j)
for i in range(l):
  if i in idx: #집합에 들어있는 인덱스 자리에 ?를 출력한다
    print('?', end='')
  else:
    print(arr[0][i], end='')