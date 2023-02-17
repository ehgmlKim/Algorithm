n = int(input())
arr = []
for i in range(n) :
  num, str = input().split()
  arr.append((num, str))
for e in arr:
    for s in e[1]:
        print(s*int(e[0]), end='')
    print()