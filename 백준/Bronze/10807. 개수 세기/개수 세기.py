n = int(input())
a=input().split()
for i in range(n):
    a[i] = int(a[i])

v = int(input())
count = 0
for e in a:
    if e==v:
        count += 1

print(count)