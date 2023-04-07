import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
s = input()
p_n = 'I' + 'OI'*n
cnt = 0
for i in range(m-2):
  if p_n == s[i:i+2*n+1]:
    cnt += 1
print(cnt)