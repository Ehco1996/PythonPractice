'''
抽象工厂模式：
抽象工厂模式是围绕一个超级工厂创建其他的工厂，该超级工厂有成为其他工厂的工厂，
这种类型的设计模式属于 创建形模式，他提供了一种创建对象的最佳方式

在抽象工厂模式中，接口只负责一个相关对象的工厂，不需要显示指定他们的类。
每个生成的工厂都能够 按照工厂模式提供对象

主要解决了： 接口选择的问题

使用场景举例：qq换肤程序， 一整套平台一起换肤，生成不同操作系统的皮肤程序

'''

import random


class PetShop(object):
    '''PetShop 是一个超级工厂，主要作用为其他宠物类工厂提供接口 '''
    def __init__(self, animal_factory=None):
        ''' pet_factory 是一个抽象的工厂 '''
        self.pet_factory = animal_factory

    def show_pet(self):
        '''通过对应的抽象工厂创建，展现宠物'''
        pet = self.pet_factory.get_pet()
        print('we have a lovely {}'.format(pet))
        print('it will say:{}'.format(pet.speak()))
        print('we also have {}'.format(self.pet_factory.get_food()))


'''通过工厂生产出来的东西'''


class Dog(object):

    def speak(self):
        return 'woof'

    def __str__(self):
        return "Dog"


class Cat(object):

    def speak(self):
        return 'meow'

    def __str__(self):
        return "Cat"


'''工厂类'''


class DogFactory(object):
    def get_pet(self):
        return Dog()

    def get_food(self):
        return 'dog food'


class CatFactory(object):
    def get_pet(self):
        return Cat()

    def get_food(self):
        return 'cat food'


def choose_factory():
    return random.choice([DogFactory, CatFactory])()

#通过PetShop这个超级工厂，关联了DogFactiry,CatFactory,同时通过接口调用了DogFactory和CatFactory的方法。
shop = PetShop(choose_factory())
shop.show_pet()
