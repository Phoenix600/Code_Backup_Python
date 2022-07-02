#import your modules here 
import pandas as pd

# define global varibale here 

# define classes here
class Person :
    def __init__(self,name,depart):
        self.name = name 
        self.depart = depart

    def Display(self):
        print(f"[+]Name             :   {self.name}")
        print(f"[+]Department       :   {self.depart}")

class Details(Person):
    def __init__(self,year,section):
       self.year        = year
       self.section     = section

    def Display(self):
        print(f"[+]Year             :   {self.year}")
        print(f"[+]Section          :   {self.section}")

class Student(Person):
    def __init__(self,name,depart,year,section,sub1,sub2):
        
        self.sub1 = sub1
        self.sub2 = sub2

        Person.__init__(self,name,depart)
        Details.__init__(self,year,section)

    def Display(self):
        Person.Display(self)
        Details.Display(self)

        print(f"Python Programming  :   {self.sub1}")
        print(f"Signal Processig    :   {self.sub2}")


# define funciton here 

# write main code here 

if __name__ == "__main__" :
    
    # creating the object here
    Pranay = Student("Pranay Ramteke","ETC",2,"B",99,100)
    Pranay.Display()
