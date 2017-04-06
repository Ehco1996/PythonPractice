a = {'周浩': 4, '真': 3}


for i in list(a):
    if len(i) <=1:
        del a[i]



print(a)
