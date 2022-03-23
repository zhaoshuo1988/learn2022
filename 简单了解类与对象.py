class Student:
    '''以两个下划线__（读作"dunder")开头和结尾的方法
       通常都有特殊的用途和意义，'''

    #__slots__=('name','age')

    '''Python中可以动态为对象添加属性，如果不希望使用对象是
       动态添加属性可使用__slots__魔法。例如__slots__=('name','age')
       则该类只能有name和age属性。动态添加则会引发异常'''

    
    def __init__(self,name,age):
        '''初始化方法
          用__init__()方法为对象指定属性
          同时完成对属性赋予初始值的操作'''
        self.__name = name   #给当前类添加属性
        self.__age = age

        
    '''对象属性会有被设置为私有（private)或受保护(protected)的成员
      不允许被直接访问。对象的方法通常是公开的(public)
      Python中用对象属性名前加前缀下划线来说明属性访问可见性
      例如可用__name表示一个私有属性，_name表示一个受保护属性'''

  #装饰器，先获取私有属性
    @property
    def name(self):
        return self.__name
    #修改私有属性
    @nam.setter
    def nam(self,name):
        self.__name=name or '无名氏'

    def age(self):
        return self.__age

    #静态方法，调用时不用先实例化
    #装饰器  @staticmethod
    @staticmethod
    def is_adult(age):
        '''判断是否成人'''
        return age > 18
    #类方法
    @classmethod
    def is_Adult(cls,age):
        '''判断是否成人'''
        return age > 18


    def __repr__(self):
        #设置打印类信息
        return f'{self.__name}:{self.__age}'

   
    
    #如果函数在类中，则被称之类方法
    def study(self,course_name):
        '''学习'''
        print(f'{self.__name}正在学习{course_name}.')

    def play(self):
        '''玩耍'''
        print('%s正在玩游戏'%self.__name)

        



#当前sut1 是Student类中的一个具体的实例

#想要调用类方法，必须先对类进行实例化

stu1=Student('詹三',20)
stu2=Student('晚五',60)
Student('李四',18).study('属性')


stu2.play()

'''Python 并没有从语法上严格保证私有属性的私密性，
只是给私有属性和方法换了个名字来阻挠对它们的访问。
如果知道更换名字的规则仍然可以访问他们，
只需对代码稍加修改即可。'''

stu1.nam=55
print(stu1.ag,stu2.nam)
print(Student.is_Adult(20))
print(hex(id(stu1)),hex(id(stu2)))
        
