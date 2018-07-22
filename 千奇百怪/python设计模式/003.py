'''
建造者模式：
建造者模式 使用多个简单的单一对象，一步一步构建一个复杂的对象，
这种类型的设计模式术语：创建形模式，他提供了一种创建对象的最佳方式
一个Builder类会一步一步的构造最终的对象，并且该Budilder类是独立于其他对象的

主要解决：
在软件系统中，有时候面临这个一个复杂对象的创建工作，其通常由各个部分的子对象用一定的算法构成
由于需求的变化，这个复杂对象的各个部分面临着剧烈的变化，但他们组合在一起的算法却是选好对稳定的

使用场景：
需要生产的对象 具有复杂的内部结，并且对象的内部属性相互依赖

'''

class Director(object):
    
    def __init__(self):
        self.builder = None

    def construct_building(self):
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()

    def get_buildings(self):
        return self.builder.building

    
'''抽象的建造者'''
class Builder(object):
    def __init__(self):
        self.building =None
    
    def new_building(self):
        self.building = Building()
    
    def build_floor(self):
        raise NotImplementedError
    
    def build_size(self):
        raise NotImplementedError

'''具体建造者'''
class BuilderHouse(Builder):
    def build_floor(self):
        self.building.floor = "one"
    
    def build_size(self):
        self.building.size = 'big'

class BuilderFlat(Builder):
    def build_floor(self):
        self.building.floor = "more than one"
    
    def build_size(self):
        self.building.size = 'samll'

''' 生产 '''
class Building(object):
    def __init__(self):
        self.floor = None
        self.size = None

    def  __repr__(self):
        return 'Floor :{0.floor} \t Size :{0.size}'.format(self)

if __name__ == '__main__':

    #建造者对象
    director = Director()
    # 调用建造者的 具体建造者 ，
    director.builder = BuilderHouse()
    # 链式调用了 抽象建造者Builder的方法 生成了 floor 和 size
    director.construct_building()
    #返回建造好的building
    building = director.get_buildings()
    print (building)

