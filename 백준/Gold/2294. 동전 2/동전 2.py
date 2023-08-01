import sys
input = sys.stdin.readline

n,k = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(int(input()))

dp = [10001] * (k+1)
dp[0] = 0

for a in arr:
  for i in range(a, k+1):
    dp[i] = min(dp[i], dp[i-a]+1)

  #print(dp)
if dp[k]== 10001:
  print(-1)
else:
  print(dp[k])