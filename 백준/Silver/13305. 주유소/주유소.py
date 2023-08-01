import sys
input = sys.stdin.readline

n = int(input())
len = list(map(int, input().split()))
price = list(map(int, input().split()))
answer = 0
요금 = price[0]
for i in range(n-1):
  if price[i] < 요금:
    요금 = price[i]
  answer += 요금*len[i]

print(answer)