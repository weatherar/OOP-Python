# multiple inherintance
class A:
    def method_A(self):
        print('ini adalah method a')

class B:
    def method_B(self):
        print('ini adalah method b')
               
class C(A, B):
    pass

object = C()
object.method_A()
object.method_B()