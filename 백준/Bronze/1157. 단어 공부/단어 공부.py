str = input()
str = str.upper()
dict = {}
for s in str:
    if s not in dict:
        dict[s] = 1
    else:
        dict[s] += 1
dict = sorted(dict.items(), key = lambda x : x[1], reverse = True)

if len(dict)>1 and dict[0][1] == dict[1][1]:
    print('?')
else:
    print(dict[0][0])