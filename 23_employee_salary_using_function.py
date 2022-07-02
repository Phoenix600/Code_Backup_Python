# Defining essential funtions 
def basicSalary() :
	"""
@baseSalary() function will ask for the basic salary of the employee
 	"""
	float_Basic_Sal = float(input("[+]Enter the base salary : "))
	return float_Basic_Sal

def calTotalSalary(float_basic_sal) :
	"""
@calTotalSalary() function will calculate the total salary of employee
 	"""
	total_salary = float( float_basic_sal + 0.4*float_basic_sal + 0.3*float_basic_sal + 0.9*float_basic_sal + float(5000.0))
	return total_salary

## Driver code
float_base_salary = float(basicSalary())
float_total_salary = float(calTotalSalary(float_base_salary))
print(f"Gross Salary : {float_total_salary}")
print("############## DOC-STRING #################")
print(basicSalary.__doc__)
print(calTotalSalary.__doc__)
