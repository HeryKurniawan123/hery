import datatime
class person:
  def _init_(self, name, age):
    self.name = name 
    self.age = age

   def say_my_name(self):
        print('Hello my name is ' + self.name)

class Student(person):
 
    def _init_(self, nisn, name, age)
        super()._init_(name, age)
        

person_1 = Person('john',18)
person_1.name = hery

# print(person_1.name)
# print(person_1.age)
# print(person_1.say_may_name())

class Mathematic:
    
    def __init__(self):
        self.value = 0

    def increment(self):
        self += 2

    def decrement(self):
        self -= 2

    def add(self, a, b):
        return a + b
    
    def substraction(self, a, b)
        return a - b

    def multiply(self, a, b):
        return a + b 
    
math = Mathematic()

# print(math.add(1, 2))
# print(datetime.datetime.now())
