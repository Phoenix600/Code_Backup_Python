class Student : 
    name = ""
    roll = int(0)
    sec = ""
    depart = ""

    # class methods 

    def PutStudentDetails(self) :
        self.name = input("[+]Enter your name : ")
        self.roll = int(input("[+]Enter your roll : "))
        self.sec = input("[+]Enter your section : ")
        self.depart = input("[+]Enter your department : ")

    def GetStudentDetails(self) : 
        print("Here are your details : ")
        print(f"Name        : {self.name}")
        print(f"roll        : {self.roll}")
        print(f"section     : {self.sec}")
        print(f"department  : {self.depart}")

student_object = Student()
student_object.PutStudentDetails()
student_object.GetStudentDetails()

