while True:
  arr = list(map(int, input().split()))
  arr = sorted(arr)
  if 0 ==arr[0]==arr[1]==arr[2]:
    break
  if arr[0]**2+arr[1]**2 == arr[2]**2:
    print('right')
  else:
    print('wrong')