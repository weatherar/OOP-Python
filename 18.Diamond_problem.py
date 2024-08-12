# diamond problem
class A:
    def show(self):
        print('ini adalah show A')
        
class B(A):
    # def show(self):
    #     print('ini adalah show B')
    pass
    
class C(A):
    # def show(self):
    #     print('ini adalah show C ')
    pass
 
class D(B, C):
    pass

object = D()
object.show()

# help(object)