# define modules here
import pandas as pd
# define global variables here 

# define class here 
class EmployeeDetails :
    """
    class EmployeeDetails <class-Type>  user-defined class
    [Class]                     [Details]
    class EmployeeDetails   :   
                                [Mannual]
                                The following class has the class-variables as Basic Sal, 
                                HRA,TA,DA,incentive,Total Salary
                                
                                [Methods]
                                @SetEmployeeDetails(self) : This function sets class-variable of the employee details 
                                @GetEmployeeDetails(self) : This function prints the employee details 
                                @CalTotalSalary(self)     : This function calculate the total salary of the passed object
    """
    basicSal    =   float(0)
    hra         =   float(0)
    ta          =   float(0)
    da          =   float(0)
    inc         =   float(0)
    total       =   float(0)

    def SetEmployeeDetails(self):
        """@SetEmployeeDetails(self) : This function sets class-variable of the employee details """
        print("[+]Enter the following details > ")
        self.basicSal       = float(input("[1]Basic Salary    : "))
        self.hra            = float(input("[2]Hra             : "))
        self.ta             = float(input("[3]TA              : "))
        self.da             = float(input("[4]DA              : "))
        self.inc            = float(input("[5]Incentive       : "))
    
    def CalTotalSalary(self):
        """
        [Methods]                   [Mannual]
        @CalTotalSalary(self)     : This function calculate the total salary of the passed object
        """
        self.total      = float((self.basicSal) + (self.hra * self.basicSal) + (self.ta * self.basicSal) + (self.da * self.basicSal) + (self.inc))

    def GetEmployeeDetails(self):
        """@GetEmployeeDetails(self) : This function prints the employee details """
        print(f"Employee Details    :")
        print(f"""
Basic Salary            : {self.basicSal}
HRA                     : {self.hra}
TA                      : {self.ta}
DA                      : {self.da}
Incentive               : {self.inc}
Total Salary            : {self.total}
        """)

# write main code here 

# empty list of employees 
employee = []
n_Employee = int(input("[+]Enter the number of Employees to put details : "))

for COUNT in range(0,n_Employee) :
    emp_Object  = EmployeeDetails()
    employee.append(emp_Object)
    employee[COUNT].SetEmployeeDetails()
    employee[COUNT].CalTotalSalary()

for COUNT in range(0,n_Employee):
    employee[COUNT].GetEmployeeDetails()


print(employee)
