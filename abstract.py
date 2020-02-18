from abc import ABC, abstractmethod

class A(ABC):
    a='herry'
    @abstractmethod
    def display(self):
        pass

class B(A):
    def display(self):
        print("This is example of abstract class")

class C(A):
    def display(self):
        print("C")


obj = B()
obj.display()
print(obj.a)

obj1 = C()
obj1.display()
