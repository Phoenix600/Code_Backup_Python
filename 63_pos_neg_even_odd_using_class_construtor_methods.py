# import moudles here


# deifne class here

class NumberAnalysis : 
    """ @NumberAnalysis of <user-defined-type>  analizes the number series into 
    [1] number of positve number in object
    [2] number of negative number in object
    [3] number of zeros in object 
    [4] number of even numbers in object
    [5] number of odd number in object 
    """
    class_pos   = int(0)
    class_neg   = int(0)
    class_zero  = int(0)
    class_even  = int(0)
    class_odd   = int(0)

    def __init__(self):
        """@__init__ initializer as constructor initilizes the object with the series or  list of numbes """
        self.list   = (input("[+]Enter the list of number to analize the list : ").split())

    def Analysis(self):
        
        for INDEX in range(0,len(self.list)-int(1)):
            """converting the given list into integer list """
            self.list[INDEX] =  int(self.list[INDEX]) 

        for INDEX in range(0,len(self.list)-int(1)):
            if self.list[INDEX] > 0 :
                NumberAnalysis.class_pos += int(1)
                if self.list[INDEX]%2 == 0 :
                    NumberAnalysis.class_even += int(1)
                else :
                    NumberAnalysis.class_odd += int(1)

            elif self.list[INDEX]< 0:
                NumberAnalysis.class_neg += int(1)
                if self.list[INDEX]%2 == 0 :
                    NumberAnalysis.class_even += int(1)
                else :
                    NumberAnalysis.class_odd += int(1)
            else :
                NumberAnalysis.class_zero += int(1)

        print(f"""
Positives   :   {NumberAnalysis.class_pos}
Negatives   :   {NumberAnalysis.class_neg}
Zeros       :   {NumberAnalysis.class_zero}
Even        :   {NumberAnalysis.class_even}
Odd         :   {NumberAnalysis.class_odd}
                """)
#creating the object of the class NumberAnalysis 

NumberSeries = NumberAnalysis()
NumberSeries.Analysis()
