class Hero:

  power = "invisibility",
  
  def __init__(self,name,age,job):
    self.name = name
    self.age = age
    self.job = job

  def method(self):
    print(f"I'm a hero and my age is {self.age}")

superman = Hero("Clark Kent", 30, "journalist")
superman.name ## Clark Kent
superman.power = "fly"
superman.power ## fly
superman.method() ## I'm a hero and my age is 30
