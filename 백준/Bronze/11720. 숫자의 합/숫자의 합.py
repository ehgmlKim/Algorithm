n=int(input())
arr=int(input())
sum = 0
for i in range(n):
    sum+=arr%10
    arr = arr//10
print(sum)