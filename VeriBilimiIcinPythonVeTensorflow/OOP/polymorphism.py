class Apple():
    def __init__(self,name):
        self.name = name

    def information(self):
        return self.name + " is 100 calories "

class Banana():
    def __init__(self,name):
        self.name = name
        
    def information(self):
        return self.name + " is 150 calories "

apple = Apple("apple")
apple.information()   ## 'apple is 100 calories '
banana = Banana("banana")
banana.information()   ## 'banana is 150 calories '

fruitList = [apple, banana]

for fruit in fruitList:
    print(fruit.information())   ## apple is 100 calories \nbanana is 150 calories 
  
def getInfo(fruit):
    print(fruit.information())

getInfo(banana)   ## banana is 150 calories 
getInfo(apple)   ## apple is 100 calories 
