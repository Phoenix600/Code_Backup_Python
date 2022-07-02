# defining the class 
import pandas as pd

class student() :
    # definig the class var
    name = ""
    year = ""

    #defining the  methods
    def setVal(self):
        '''setting the value of data members '''
        self.name = input("[+] Enter name : ")
        self.year = int(input("[+] Enter year : "))

    def getVal(self):
        "displaying the value"

object = student()
object.setVal()
df = pd.DataFrame(object)
