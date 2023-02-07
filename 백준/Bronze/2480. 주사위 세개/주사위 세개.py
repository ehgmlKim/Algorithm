a,b,c=map(int, input().split())

if a==b and a==c :
    print(10000+a*1000)
elif a==b and a!=c:
    print(1000+a*100)
elif a==c and a!=b :
    print(1000+a*100)
elif b==c and a!=b :
    print(1000+b*100)
else:
    max = a if a>b else b
    max = max if max>c else c
    print(max*100)