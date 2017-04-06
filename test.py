a = {'the': 4, 'a': 3}
b = ['the']

for ex in b:
    if ex in a.keys():
        del a[ex]




print(a)
