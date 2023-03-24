import sys
input = sys.stdin.readline
dict = {0:'zero ', 1:'one ', 2:'two ', 3:'three ', 4:'four ', 5:'five ', 6:'six ', 7:'seven ', 8:'eight ', 9:'nine '}

m, n = map(int, input().split())
arr_dict = {}

for num in range(m, n+1):
  s = ''
  for i in str(num):
    s += dict[int(i)]
  arr_dict[num] = s
#print(arr_dict)
arr_dict = sorted(arr_dict.items(), key = lambda x:x[1])
#print(arr_dict)
i = 0
for k in arr_dict:
  if i==10:
    i = 0
    print()
  print(k[0], end=' ')
  i += 1
  