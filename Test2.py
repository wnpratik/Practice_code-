from dataclasses import dataclass

@dataclass

class Rectangle:
    width:int
    height:int
    colors:str

rectangle1=Rectangle(2,3,'black')   
print(rectangle1.width)


@dataclass
class Person:
    name:str
    age:int
    salary:float

person1=Person("Pratik",30,1.5) 

print(person1.name)
print(person1.age)
print(person1.salary)
