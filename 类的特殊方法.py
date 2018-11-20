class  User:
    '''
    这是注释
    '''
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def run(self):
        print('在跑，%s'%self.name)

    def __call__(self, *args, **kwargs):
        print('这是通过call方法调用的')

    def __str__(self):
        return '你好'

which = User('ywy',25)
#hasattr 判断对象有没有属性/方法,返回布尔值
re = hasattr(which,'name')
print(re)

#getattr 获取对象的属性和方法   如果有name这个属性就输出上面的ywy，如果没有这个属性，有第三参数的话，就输出第三参数的值
re = getattr(which,'name')   #如果又没设置第三个参数，又没这个属性的话会抛出异常错误。
print(re)

#setattr   设置一个不存在的属性  若存在就修改
setattr(which,'name','xiaoming')

#delatte  删除属性,不存在会报错。
delattr(which,'name')
print(hasattr(which,'name'))

#判断这个实例化对象是不是这个类的实例。
print(isinstance(which,User))

#特殊方法：
print(which.__doc__)  #输出注释。
print(which.__dict__)    #输出实例化对象的属性。  以字典的形式返回{’age‘: 25}
which()   #会调用call方法   实例化对象+()可以调用call方法
print(which)  #直接print 实例化对象 可以打印str里面的方法。









