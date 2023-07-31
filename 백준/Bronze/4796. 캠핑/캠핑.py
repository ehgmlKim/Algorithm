import sys
input = sys.stdin.readline
i = 1
while True:
  L,P,V=map(int, input().split())
  if L==0 and P==0 and V==0:
    break
  answer = V//P*L + min(V%P, L)
  print("Case %d:" %i,answer)
  i += 1