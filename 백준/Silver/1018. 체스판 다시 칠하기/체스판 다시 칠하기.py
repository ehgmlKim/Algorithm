import sys
input = sys.stdin.readline
m,n = map(int,input().split())
c=[]
answer = []
# w가 첫번째 일때
cw=[['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W']]
#B 가 첫번째 일때
cb=[['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B']]
for _ in range(m):
  c.append(list(input()))

for i in range(m-7):
  for j in range(n-7):
    cnt1, cnt2 = 0, 0
    for a in range(i, i+8):
      for b in range(j, j+8):
        if c[a][b] != cw[a-i][b-j]:
          cnt1 += 1
    for a in range(i, i+8):
      for b in range(j, j+8):
        if c[a][b] != cb[a-i][b-j]:
          cnt2 += 1
    answer.append(cnt1)
    answer.append(cnt2)
print(min(answer))