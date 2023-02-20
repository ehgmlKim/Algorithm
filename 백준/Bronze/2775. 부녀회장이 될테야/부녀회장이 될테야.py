T = int(input())
for _ in range(T):
  floor = int(input())
  room = int(input())
  answer = [i+1 for i in range(room)]
  for f in range(floor):
    for r in range(1, room+1):
      if r==1:
        answer += [1]
      else:
        answer += [answer[-1]+answer[r-1+room*f]]
  print(answer[-1])