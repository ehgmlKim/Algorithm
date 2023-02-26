n = int(input())
card = {}
card_arr = map(int, input().split())
for c in card_arr:
  if c not in card:
    card[c] = 1
  else:
    card[c] += 1
m = int(input())
find = map(int, input().split())
for f in find:
  try:
    print(card[f], end=' ')
  except:
    print(0, end=' ')