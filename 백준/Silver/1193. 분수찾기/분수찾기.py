n=int(input())
cnt = 0
i = 0
while cnt<n:
  i += 1
  cnt += i
  
idx = n-cnt+i
sum = i+1
if sum%2!=0:
  print(str(idx)+'/'+str(sum-idx))
else:
  print(str(sum-idx)+'/'+str(idx))
