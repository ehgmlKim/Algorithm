import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dict = {}
for i in range(n):
  dict[input().rstrip()] = i+1
dict_arr = list(dict.items())

for _ in range(m):
  x = input().rstrip()
  if x.isalpha(): #문자면
    print(dict[x])
  else:
    print(dict_arr[int(x)-1][0])
    