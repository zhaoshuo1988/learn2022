class Animal:

    def __init__(self,name):
        self.name=name


    def eat(self):
        print('Animal吃母乳')

    #私有方法
    def __drink(self):
        print('喝水')

    def run(self):
        print('跑')

        #在公有方法中调用私有方法
        self.__drink()
        

'''新建类继承Animal 继承公有属性和方法'''
class Bird():
    
    def bark(self):
        print('汪汪叫')

    def eat(self):
        print('Bird吃虫子')
'''多继承会继承父类所有的父类方法和属性'''
class 德牧(Animal,Bird):
    def fly(slef):

        
        print('我会飞')
        super().eat()

    def eat(self):
        #重写父类方法
        print('像德牧一样吃')

        #在当前方法中调用父类方法使用super()方法
        #或者父类名.父类方法(self)。Python2常用，Python 3不推荐
        super().bark()
        Animal(self).run()


旺财=德牧('旺财')
旺财.bark()
旺财.eat()
旺财.fly()
print(德牧.__mro__)        #mor搜索调用方法查询顺序
