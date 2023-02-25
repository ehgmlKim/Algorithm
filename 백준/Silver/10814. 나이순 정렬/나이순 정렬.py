n = int(input())
dict = {}
for i in range(n):
    dict[i] = input().split()

dict = sorted(dict.items(), key = lambda x : int(x[1][0]))
for k,v in dict:
    print(v[0], v[1])