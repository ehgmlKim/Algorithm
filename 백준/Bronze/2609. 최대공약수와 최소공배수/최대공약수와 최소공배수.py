a, b = map(int, input().split())

gcd, lcm = 0, 0
for i in range(min(a,b)+1, 0, -1):
  if a%i==0 and b%i==0:
    gcd = i
    break
lcm = a*b//gcd
print(gcd)
print(lcm)