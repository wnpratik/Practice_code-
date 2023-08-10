def welcome():
    return("Welcome to Amazon")

welcome()    
welcome()
welcome() 

msg=welcome()
print(msg+"Pls like")

### Odd and Even Nos Prog:-

def even_odd_sum(lst):
    even_sum=0
    odd_sum=0
    for i in lst:
        if i%2==0:
            even_sum+i
        else:
            odd_sum+i
    return even_sum,odd_sum

sum1,sum2=even_odd_sum([1,2,3,4,5,45,6678,8])       

print(sum1,sum2)

### Init Functions

class Car:
    def __init__(self,window,carenginetype,door):
        self.window=window
        self.carenginetype=carenginetype
        self.door=door
    def driving(self):
        print("Car is used for driving")
## Audi class inhiriting the calrclass
class Audi(Car):
    def __init__(self, window, carenginetype, door, sunroof,horsepower):
        super().__init__(window,carenginetype,door)
        self.sunroof=sunroof
        self.horsepower=horsepower

audiq7=Audi(3,"Diesel",4,"Black", 200) 
print(audiq7.sunroof)
print(audiq7.carenginetype)
print(audiq7.horsepower)
print(audiq7.driving())      

print(dir(audiq7))
