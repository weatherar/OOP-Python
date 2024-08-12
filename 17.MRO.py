# method resolution order //muliple inherintance

class A:
    def show(self):
        print("I am from class A")

class B:
    def show(self):
        print("I am from class B")


class C(B,A):
    # def show(self):
    #     print("I am from class C ")
    pass

object = C()
object.show()
# help(object)