n=int(input())
arr=list(map(int, input().split()))
m = max(arr)
sum = 0
for e in arr:
    e = e/m*100
    sum += e
print(sum/n)