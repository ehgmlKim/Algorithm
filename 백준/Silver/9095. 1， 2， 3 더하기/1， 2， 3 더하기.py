import sys
input = sys.stdin.readline

n = int(input())

# 1 => 1
# 2 => 2
# 3 => 4
# 4 => 7
dp = [0 for _ in range(11)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
for _ in range(n):
  m = int(input())
  
  for x in range(4, m+1):
    dp[x] = dp[x-1] + dp[x-2] + dp[x-3]
  print(dp[m])
  