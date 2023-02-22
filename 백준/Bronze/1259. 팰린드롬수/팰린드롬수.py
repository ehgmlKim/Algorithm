while True:
  n = input()
  if not int(n):
    break
  if n[::1] == n[::-1] :
    print('yes')
  else:
    print('no')