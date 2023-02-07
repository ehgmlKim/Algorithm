a = [ i for i in range(1, 31)]

for i in range(28):
    x = int(input())
    a.remove(x)

print(min(a))
print(max(a))