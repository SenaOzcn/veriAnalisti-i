class Fruit():
    def __init__(self,name,cal):
        self.name = name
        self.cal = cal

    def __str__(self):
        return f"{self.name} is {self.cal} calories."

    def __len__(self):
        return self.cal

banana = Fruit("banana",150)
banana.cal   ## 150
print(banana)   ## banana is 150 calories.
myList = [1, 2, 3, "a", 4.5]
print(myList)   ## [1, 2, 3, 'a', 4.5]
len(myList)   ## 5
len(banana)   ## 150
apple = Fruit("apple", 200)
print(apple)   ## apple is 200 calories.
