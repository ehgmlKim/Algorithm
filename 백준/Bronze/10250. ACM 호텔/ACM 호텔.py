t = int(input())
for _ in range(t):
  h,w,n = map(int, input().split())
  floor = n%h if n%h != 0 else h
  room = n//h+1 if n%h != 0 else n//h
  print(floor*100+room)