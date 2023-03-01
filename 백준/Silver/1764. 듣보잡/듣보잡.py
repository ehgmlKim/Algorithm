import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dict = {}
for _ in range(n+m):
  x = input()
  if x not in dict:
    dict[x] = 1
  else:
    dict[x] += 1
answer = sorted([k for k,v in dict.items() if v==2])
print(len(answer))
print(''.join(answer))
