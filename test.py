class Student():
    def __str__(self):
        return "1"
    pass

def test(parm='123'):
    a = dict(parm = Student)
    print(a[parm]())    
    return a

test()
