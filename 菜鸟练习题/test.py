def func(a, b):
    c = a**2 + b
    b = a
    return c
a = 10
b = 100
c = func(a, b) + a

print(c)
print(a,b)