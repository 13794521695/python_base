class  Aminal:     #默认集成object
    #类属性   和实例化属性的区别在于类属性不用self，而实例化属性要self， 类属性可以被实例化属性调用，也可以被类属性调用
    __eye = 2
    b = 10
    leg = []
    def __init__(self,name,age):  #实例化一个方法，在类实例化的时候被调用。
        self.name = name
        self.age = age
    def run(self):
        print('在跑------')

#调用
a = Aminal('ywy',25)
#print(a.run())  #打印的时候会把return None也打印过来
#a.run()
print(a.name,a.age)
#调用类属性： 以下两种结果都一样。
a.__eye =10   #实例化
print(a.__eye)
print(a._Aminal__eye)       #双下划线的话就要这样才能访问，
#print(Aminal.eye)
#设置属性
a.sum = 3   #类实例化的对象创建的属性不可以被类访问，类创建的属性却可以被实例化对象访问
#print(a.sum)
#实例化去修改leg（列表）,  类属性的leg也会变,  但是实例化去修改eye，类属性的eye不会变
#._eye=10
#print(a.eye)
#rint(a._eye)


#总结，类就相当于一个模板， 实例化对象就相当于在这个模板上创建的物体， 可以具备模板的属性，也可以增加自己的属性。