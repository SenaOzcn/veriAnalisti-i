class Hero():

    power = "invisibility"
    
    def __init__(self,name,age,job):
        print("called the init")
        self.name = name
        self.age = age
        self.job = job

    def method(self):
        print(f"I'm a hero and my job is {self.job}")
        print(f"I'm a hero and my age is {self.age}")

superman = Hero("Clark Kent",30,"journalist")   ## called the init
superman.name   ## 'Clark Kent'
superman.power = "flying"
superman.power   ## 'flying'
superman.method()   ## I'm a hero and my job is journalist I'm a hero and my age is 30
