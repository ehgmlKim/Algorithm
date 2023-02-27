str = input()
new = ''
for s in str:
    if s.isupper():
        new += s.lower()
    else:
        new += s.upper()
print(new)