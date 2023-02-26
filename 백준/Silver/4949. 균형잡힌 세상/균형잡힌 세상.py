while True:
  str = input()
  check = []
  answer = 'yes'
  if str == '.':
    break
  for s in str:
    if s=='(' or s=='[':
      check.append(s)
    elif s == ')':
      if not len(check): # ( 괄호가 나오기 전에 닫힌 괄호가 나온 경우
        answer = 'no'
        break
      else:
        if check.pop(-1) != '(':
          answer = 'no'
          break
    elif s == ']':
      if not len(check): # ( 괄호가 나오기 전에 닫힌 괄호가 나온 경우
        answer = 'no'
        break
      else:
        if check.pop() != '[':
          answer = 'no'
          break
    else:
      continue
  if len(check):
    answer = 'no'
  print(answer)