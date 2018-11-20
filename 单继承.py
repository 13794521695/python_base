#子类继承父类的所有功能。
#单继承
class A:
    eye = 2
    _boy = 'nan'
    __girl = 'nv'
    def fxl(self):
        print('A')
class B(A):
    def fxl(self):
        print('B')
class C(B):
    def fxl(self):
        print(super().fxl())
        print('C')
class D(C):
    def fxl(self):
        print(super(B,self).fxl())   #super里没参数，默认调用父类的方法，如果父类也没这个方法就会到父类的父类去找，直到找到
        print('D')                   #为止,当super里有参数时，则调用参数的父类方法
d = D()
d.fxl()
# print('fdsfds')