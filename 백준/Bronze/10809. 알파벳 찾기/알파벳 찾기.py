s=str(input())
alpa='abcdefghijklmnopqrstuvwxyz'
for e in alpa:
    if e in s:
        print(s.index(e), end=' ')
    else:
        print(-1, end=' ')
    