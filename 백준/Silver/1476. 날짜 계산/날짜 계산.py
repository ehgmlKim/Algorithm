import sys

input = sys.stdin.readline
E,S,M = map(int, input().split())
e,s,m,year = 0,0,0,0
def func(e,s,m):
  e = e+1 if e+1<=15 else (e+1)%15
  s = s+1 if s+1<= 28 else (s+1)%28
  m = m+1 if m+1<=19 else (m+1)%19
  return e, s, m
while True:
  e,s,m = func(e,s,m)
  year += 1
  if E==e and S==s and M==m:
    break
print(year)