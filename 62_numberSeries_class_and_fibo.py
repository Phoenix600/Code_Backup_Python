# define modules here 

# define class here 
class NumberSeries :
    """Defing the class of NumberSeries of <user-defined-type> c """
    n_objects = int(0)

#    def __init__(self,first_term,second_term,n_terms):
    def __init__(self):
        """@__init__() defining the constructor to initialize the object  """
        self.first_term          = int(input("[+]Enter the first term of the sequence  : "))
        self.second_term         = int(input("[+]Enter the second term of the sequence : "))
        self.n_terms             = int(input("[+]Enter the number terms to display     : "))
        self.commanDifference    = int(input("[+]Enter the command difference in case of AP-Series:")
        self.commonRatio         = int(input("[+]Enter the comman ratio in case of GP-series : "))
   
    def Arithmatic(self):
        """@Arithmatic method to print the arithmatic series for the given terms and comman difference  """
        

    def Fibbonacci(self):
        print(self.first_term,end=" ")
        print(self.second_term,end = " ")
        for TERMS in range(0,self.n_terms):
            self.next_term      = self.first_term + self.second_term
            self.first_term     = self.second_term
            self.second_term    = self.next_term
            print(self.next_term,end=" ")


FibSeries = NumberSeries()
FibSeries.Fibbonacci()

