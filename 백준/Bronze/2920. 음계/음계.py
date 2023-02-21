str = input().split()

if sorted(str) == str:
    print('ascending')
elif sorted(str, reverse = True) == str:
    print('descending')
else:
    print('mixed')