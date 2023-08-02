import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*n
arr = [int(input()) for _ in range(n)]

if n<=2:
  print(sum(arr))
else:
  dp[0] = arr[0]
  dp[1] = arr[0] + arr[1]
  for i in range(2,n): # 3번째 계단 부터 dp 점화식 이용해서 최대값 구하기
    dp[i]=max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])
  print(dp[-1])