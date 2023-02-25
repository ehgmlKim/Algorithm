n = int(input())
list = []
for i in range(n):
    list.append(input().split())

list.sort(key = lambda x : int(x[0]))
for a,n in list:
    print(a, n)