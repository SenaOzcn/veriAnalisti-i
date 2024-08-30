class Animals():
    def __init__(self):
        print("animal class called")

    def method1(self):
        print("animal class method1 called")

    def method2(self):
        print("animal class method2 called")

myAnimal = Animals()   ## animal class called
myAnimal.method1()   ## animal class method1 called
myAnimal.method2()   ## animal class method2 called

class Cat(Animals):
    def __init__(self):
        Animals.__init__(self)
        print("cat class init called")

    def miaw(self):
        print("miaw")

    #override
    def method1(self):
        print("cat class method1 called")

myCat = Cat()   ## animal class called \ncat class init called
myCat.method1()   ## cat class method1 called
myCat.miaw()   ## miaw
