a=[]
for i in range(9):
    x=int(input())
    a.append(x)
idx=0
for i in range(9):
    if max(a)==a[i]:
        idx = i
print(max(a))
print(idx+1)