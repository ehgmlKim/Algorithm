arr=[]
for i in range(10):
    x=int(input())
    e = x%42
    arr.append(e)
new = set(arr)
print(len(new))