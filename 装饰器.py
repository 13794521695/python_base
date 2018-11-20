#装饰器的本质就是函数
from  functools import  wraps
def auth(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('验证权限')
        func(*args,**kwargs)
    return  wrapper

@auth            #@auth  的作用其实就是把下面的函数pub_article装到auth(pub_article)上
def pub_article(tiele):
    print('发布文章 %s'%tiele)

#print(pub_article.__name__)   #会指向wrapper

@auth
def add_comment():
    print('添加评论')

pub_article('标题1')
#
add_comment()

#pub_article('标题2')
#print(pub_article.__name__)    #这里一样会打印warpper，因为被装饰的函数被返回了wrapper，具备wrapper方法和属性


#有时候我们会单独需要用到被装饰的函数， 不希望被装饰器装饰
#解决办法from  functools import  wraps        @wraps(func)

#写一个装饰器
# def fy(func):
#     print('----1-----')
#     def fz(*args,**kwargs):
#         print('---2----')
#         return func()
#     print('----3------')
#     return  fz
#
# @fy
# def fx():                      #打印1和3
#     print('-----4----')
#     return  '你好'           #这里面的retuen要想被输出，上面的 要retuen  func()写法才可以
#
# print(fx())  #其实就是相当于fz()，因为       打印1,3,2,4
#
#
#
#类装饰器：
class Score:
    def __init__(self,score,age):
        self._score = score
        self.age = age
    @property   #这个用法是可以把方法变为属性来访问，但是不能用which.score = 19来修改，要修改必须用到@score,setter类装饰器。
    def score(self):
        return  self._score

    @staticmethod            #静态方法，相当于外面的函数拿到里面来用。
    def  test():
        print('这是测试')

    @classmethod
    def  test1(cls):
        print('efdsfrd')


which = Score(60,18)
print(which.score)
print(which._score)
which.test()
which.test1()
# Score.test1()
#
# #类方法   无论是静态方法还是类方法都是类去访问的。  类方法是由类去访问，与类交换，不和实例化交互。
# Score.test1()
#
class Dog(object):
    name="Jerry"
    def __init__(self,name):
        self.name = name
    @classmethod
    def eat(self):
        print("%s is eating %s" %(self.name,"food"))
    def talk(self):
        print("%s is talking" % self.name)
d = Dog("Tom")
d.eat()
Dog.eat()  #只要是类方法，都是和类交互

d.talk()

