# 001
print(10 / 3 == 3)

# 002
print('C:\file\time')

# 003
print('Py' + 'thon')

# 006


def ask(prompt="Do you like Python? ", hint="yes or no"):
    while True:
        answer = input(prompt)
        if answer.lower() in ('y', 'yes'):
            print("Thank you")
            return True
        if answer.lower() in ('n', 'no'):
            print("Why not")
            return False
        else:
            print(hint)
# ask()


def test():
    a = 1
    b = 2
    c = 3
    return a, b, c


a = test()
print(a)

# 010
l = [1, 2, 3, 4]
l.insert(2, -1)
print(l)

# 011
l = [1, 2, 3, 4, 5]
del l[2:4]
print(l)

# 012
scores = {'Jack': 90, 'Mike': 80, 'Jay': 85, 'Bill': 60}
s = dict(Jack=90, Mike=80, Jay=85, Bill=60)
print(id(scores), id(s))
print(sorted(scores.keys()))

# 013
for i in enumerate(l):
    print(i)


# 015
a = {}
tuplea = ('sum')
lsita = ['sum']
lsita.sort()
#a[lsita] = 1
print(a)

# 020


def compute(*numbers):
    sum = 1
    for n in numbers:
        sum = sum * n + n
    return sum


nums = (3, 3)
print(compute(*nums))

# 025
count = 1
print(count - 1)

# 028
a = range(1, 4)
print(a)

# 029
la = [1, 2, 3]
#la[len(la)] = 4
print(la)

# 041
fp = open('test.txt', 'r+', 0)
fp.readline()
fp.seek(10, 1)
print(fp.readline())

