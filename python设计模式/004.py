'''
工厂模式：
最常用的一种设计模式，在工厂模式中，
我们在创建对象时，不会对客户端暴露创建逻辑，
并且是通过用同一个共同的接口 来指向新创建的对象

'''


class GreekGetter(object):

    def __init__(self):
        self.tarns = dict(dog='awang', cat='amiao')

    def get(self, msigid):
        return self.tarns.get(msigid, str(msigid))


class EnglishGetter(object):

    def get(self, msgid):
        return str(msgid)


#创建实例的接口
def get_localizerr(language='English'):

    languages = dict(English=EnglishGetter, Greek=GreekGetter)
    print(type(languages[language]()))
    '''
    这里返回了一个创建对象的接口！
    OUT : <class '__main__.EnglishGetter'>
    '''
    
    return languages[language]()

#实例化两种语言
e, g = get_localizerr(language='English'), get_localizerr(language='Greek')
print(e)
'''
这里已经实例化了 e 对象。并将English作为msigid参数传了进去
OUT：<__main__.EnglishGetter object at 0x106e11710>
'''

for msigid in 'dog parrot cat bear'.split():
    print(e.get(msigid), g.get(msigid))
