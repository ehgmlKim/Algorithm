import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = []
cnt = 0
for _ in range(n):
  arr.append(int(input()))
while k>0:
  arr = [x for x in arr if x<=k]
  cnt += k // arr[-1]
  k -= (k // arr[-1])*arr[-1]
print(cnt)
  
