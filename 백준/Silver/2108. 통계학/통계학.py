import sys
N = int(sys.stdin.readline())
arr=[]
sum_v = 0
max_v = -4000
min_v = 4000
for _ in range(N):
  x = int(sys.stdin.readline())
  arr.append(x)
  if x<min_v:
    min_v = x
  if x>max_v:
    max_v = x
  sum_v += x

dict = {}
for a in arr:
  if a not in dict:
    dict[a] = 1
  else:
    dict[a] += 1

#산술평균
if sum_v <0:
  print(0 - abs(sum_v//N + (1 if (sum_v/N - sum_v//N)>=0.5 else 0)))
else:
  print(sum_v//N + (1 if (sum_v/N - sum_v//N)>=0.5 else 0))
  
#중앙값
sort_dict = sorted(dict.items(), key = lambda x : x[0])
idx = 0
for d in sort_dict:
  idx += d[1]
  if idx >= N//2+1:
    print(d[0])
    break

#최빈값
max_cnt = max(list(dict.values()))
max_arr = [x[0] for x in sort_dict if x[1] == max_cnt]

if len(max_arr)>1:
  print(max_arr[1])
else:
  print(max_arr[0])

#범위
print(max_v - min_v)