#多继承
class A:
    def fn(self):
        print('A')
class B(A):
    def fn1(self):
        print('B')
class C:
    def fn1(self):
        print('C')
class D(C):
    def fn1(self):
        print('D')
class E(D,B):
    def fn1(self):
        super().fn1()
        print('E')
e = E()
e.fn1()      #执行顺序是从左到右，父类没有这方法，会到父类的父类去寻找，找不到的时候才会到右边去寻找。
print(e.__class__.mro())

