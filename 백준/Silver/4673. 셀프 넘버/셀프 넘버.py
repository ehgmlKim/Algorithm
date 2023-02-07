def d(n):
    ans = n
    while n>0 :
        ans += n%10
        n = n//10
    return ans

x=list(range(1,10001))
y=[]
for i in x:
    c=d(i)
    if c<=10000:
        y.append(c)

y=set(y)
y=list(y)

s=[a for a in x if a not in y]

for i in s:
    print(i)