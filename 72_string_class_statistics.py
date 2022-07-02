# import your modules here

# define class here 
class String : 

    def __init__(self):
        
        self.filename = input("[+]Enter teh file name to save the statistics : ")
        self.vowels     = int(0)      
        self.consonent  = int(0)   
        self.spaces     = int(0)
        self.newlines   = int(0)

        with open(self.filename,"w") as self.FILE :
            print("[+]Enter teh paragraph :")
            INPUT = ""

            while INPUT != "quit":
                INPUT = input()
                if INPUT == "quit":
                    break
                else :
                    self.FILE.write(INPUT)

    def calVowels(self) :

        # opening the files :
        with open(self.filename) as FILE :
            para    =   FILE.read()
            #for char in para :
            #print(char)
            print(type(para))

        # calculating the number of vowels and consonents 
        
        for char in para :
            
            if char in ['a','e','i','o','u','A','E','I','O','U'] :
                self.vowels +=1 
            elif char !='\n' and char !=' ':
                self.consonent +=1 

            else :
                pass

        print(f"Vowels          :   {self.vowels}")
        print(f"Consonents      :   {self.consonent}")

    def calSpaces(self):

        with open(self.filename) as FILE :
            para = FILE.read()
#            print(type(para))

            for char in para :
                if char == " " and char != '\n' :
                    self.spaces+=1
                else :
                    pass
            print(f"Space           :   {self.spaces}")

    def calNewlines(self):
        with open(self.filename) as FILE :
            para = FILE.read()

            for char in para :
                if char == '\n' :
                    self.newlines+=1
                else :
                    pass
            print(f"Newlines        :   {self.newlines}")

if __name__ == "__main__" :

    str = String()
    str.calVowels()
    str.calSpaces()


""" 
with open("userInput.txt","w")  as FILE :
    print("[+]Enter the paragraph :")

    INPUT =""
    while INPUT != "quit" :
        INPUT = input()
        if INPUT == "quit":
            break
        else :
            FILE.write(INPUT)
"""
