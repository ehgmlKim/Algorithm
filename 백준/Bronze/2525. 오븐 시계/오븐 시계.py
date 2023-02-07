h,m=map(int, input().split())
t=int(input())
th = int(t/60)
tm=int(t%60)
h=th+h
m=tm+m
if m>=60:
    h=h+1
    m=m-60
if h>=24:
    h=h-24
print(h, m)