'''
原型模式：
用原型实例指定创建对象的种类，并且用过拷贝这些原型对象来创建新的对象，
原型模式的本质就是克隆对象，所以咋对象初始化造作比较复杂的情况下，很实用
能大幅度降低耗时，提高性能，因为不用重新初始化对象，而是动态的会的对象运行是的状态

使用场景：
资源优化场景：实例化需要消耗非常多的资源，包括数据、硬件资源等，
性能和安全要求场景： 一个队向对个修改者的场景

注意：与通过一个类来进行实例化来构造新对象不同的是：原型是通过拷贝一个现有的对象生成新的对象的
 
'''

class Prototype(object):

    value = 'default'

    def clone(self,**attrs):
        obj =self.__class__()
        obj.__dict__.update(attrs)
        return obj

class PrototypeDispacher(object):
    
    def __init__(self):
        self._objects = {}
    
    def get_objects(self):
        return self._objects
    
    def register_object(self,name,obj):
        self._objects[name] = obj

    def unregister_object(self,name):
        del self._objects[name]

def main():
    dispatcher = PrototypeDispacher()
    prototype = Prototype()

    d = prototype.clone()
    a = d.clone(value='a=value',category='a')
    b = d.clone(value='b=value',is_checked=True)
    
    dispatcher.register_object('objecta',a)
    dispatcher.register_object('objectb',b)
    dispatcher.register_object('default',d)

    print([{n:p.value} for n,p in dispatcher.get_objects().items()])

if __name__ == '__main__':
    main()
    