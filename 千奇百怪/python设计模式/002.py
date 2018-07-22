'''
共享模式：brog
一个能在实例之间共享状态的单例模式，单例模式涉及到一个单一的类，
该类福贼创建自己的对象，同时确保只有 单个对象  被创建，
这个类提供了一种访问其唯一的对象的方式，这样就能直接访问，
不需要初始化该类的对象。
'''


class Borg(object):
    # 该类的私有属性，在类的外部不能访问这个属性
    _share_state = {}

    def __init__(self):
        '''Python class 通过内置的成员__dict__存储成员信息（以字典的形式）'''
        self.__dict__ = self._share_state
        self.state = 'init'

    def __str__(self):
        return self.state


class YourBorg(Borg):
    pass


if __name__ == '__main__':

    # 初始化两个brog实例
    rm1 = Borg()
    rm2 = Borg()

    rm1.state = 'Idle'
    rm2.state = 'Running'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    rm2.state = 'Zombie'
    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    rm3 = Borg()
    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))
    print('rm3: {0}'.format(rm3))

    rm4 = YourBorg()
    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))
    print('rm3: {0}'.format(rm3))
    print('rm4: {0}'.format(rm4))
    


'''
OUTPUT:
rm1: Running
rm2: Running
rm1: Zombie
rm2: Zombie
rm1: init
rm2: init
rm3: init
rm1: init
rm2: init
rm3: init
rm4: init

即所有Brog的成员都共享单一的state状态。
'''