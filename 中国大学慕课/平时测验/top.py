'''
python的高级用法

generator
iterator
class method,instance method,static method
lambda closure
*args **kwargs
magic method
list comprehension
dict comprehension
decorator
默认参数

'''


'''
generator
假设需要一口气生成一个包含1000000个数的数组用来做循环计数器
在没有生成器的版本中需要先在内存中申请足够大的空间来存放该数组
但实际上我们每次只需要一位空间来存放循环所有需要的计数
这个就导致了生成器的诞生（实际上使用携程做的）
'''


def my_range(n):
    i = 0
    while i != n:
        i += 1
        yield i

# r = my_range(1000000)
# for i in r:
#     pass


# iterator
'''
1. iter(obj) == obj.__iter__()
2. next(obj) == obj.__next__()

在Python里循环其实是这样实现的
for i in range(10):
    pass

= =

iter_obj=range(10)
iter(iter_obj)

whie True:
    try:
        i = next(iter_obj)
    except StopIteration:
        break

当一个对象实现了上述两个接口，那么这个对象就可以被视为iterator 迭代器（这也得益于Python是一个鸭子类型的语言）
'''


class Pow2():
    '''简单迭代器的实现'''

    def __init__(self, max):
        self.max = max
        self.n = 0

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.max:
            self.n += 1
            return 2**self.n
        else:
            raise StopIteration


# p = Pow2(10)
# for i in p:
#     print(i)

'''
class method,instance method,static method

instance method: A() a.foo() a.bar() 实例方法
class method:    A.s_foo()   类方法
static method： find（）  一般只在类内使用，没有固定的默认参数（为了严谨）静态方法

引用类型
[]{}

深拷贝 浅拷贝
# 第一种陷阱
from copy import deepcopy
l1 = []
l2 = deepcopy(l1)
l1.append(1)
print(l2)

# 第二种陷阱
def foo(a=[]):
    a.append(1)
    print(a)
foo()
foo()
'''


class A():
    @staticmethod
    def find():
        pass

    @classmethod
    def s_foo(cls):
        pass

    def foo(self):
        pass


'''
lambda
匿名函数 闭包
好处：
1 适配算法 algorithm sort(lambad x:x['key'])
2 map reduce filter
'''

# print(list(map(lambda x: 3 * x, [1, 2, 3])))
# print(list(filter(lambda x: x % 3 == 0, [1, 2, 3])))
# import functools
# import operator
# print(functools.reduce(operator.add, [1, 2, 3], 5))

'''
closure ref
闭包
'''


def greeting(msg):
    '''hello 就是这里的闭包'''
    def hello(name):
        print(msg, name)
    return hello


# h = greeting('hahah')
# h('ehco')

l = []
for i in range(10):
    def _(i=i):
        print(i)
    l.append(_)

# for f in l:
#     f()

'''
*args **kwargs
tuple
dict
*args   (a,b,c,d)
**kwargs k = v
'''


def log(*args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)


# log(1, 2, 3, 4)
# log(1, 2, [1, 3, 4], c=4)

'''
decorator
对函数包转的函数 装饰器
来自于AOP编程 面向方面编程
'''


def simple_wrapper(fn):
    def _():
        print(fn.__name__)
        return fn()
    return _


@simple_wrapper
def bar():
    pass


'''
list comprehension
列表推导
[i for i in range(10)]

dict comprehension
字典推导
{k:1 for k in range(10)}

列表生成器
(i for i in range(10))
'''


'''
magic method
__add__ 
....
....
python 内置的下划线方法

__getattribute__

__getattr__
__setattr__
missing function
'''


class LogAll():
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

    def __getattribute__(self, item):
        print(item)


class Any(object):
    def __getattr__(self, item):
        print(item)

    def __setattr__(self, key, value):
        print("set", key, value)


l = LogAll()
print(l.a)
l.a = 1
l.b
l.c
a = Any()
a.a

'''
mixin
解决了类之间的相互引用问题
'''


class A():
    def foo(self):
        print("foo")

    def bar(self):
        print("bar")
        self.shit()


class B():
    def shit(self):
        print("shit")


class C(A, B):
    pass


c = C()
c.shit()
