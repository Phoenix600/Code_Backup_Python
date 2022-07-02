""" Declaring all variable as  global varibale here and assigning to empty container according to data-types """
# Global varibales
string_name = ""  
int_emp_id = int(0)
string_depart = ""
string_desig = ""
float_base_salary = float(0)
float_gross_salary= float(0)

# Exit Condition variable
bool_choice = True

# @functions : all require functions are defined here 
def setData():
	# Acessing all global variable by using 'global' keyword
	global string_name
	global int_emp_id
	global string_depart
	global string_desig
	global float_base_salary
	global float_gross_salary

	# setting data to print employee salary
	print("[+]Enter the following details 		: ")
	string_name        = str(input("[1]Name		: "))
	int_emp_id         = int(input("[2]Employee Id 	: "))
	string_depart      = str(input("[3]Department 	: "))
	string_desig       = str(input("[4]Designation	: "))
	float_base_salary = float(input("[5]Base Salary  : "))

	# Calculating Gross Salary 
	# PF = -2500
	# TDS = -1000 
	# Incentive = +5000
	float_gross_salary = float( (0.4*float_base_salary) + (0.3*float_base_salary) + (0.9*float_base_salary)+ float_base_salary + float(5000.0) - float(2500.0) - float(1000.0))
	

def getData():

	# Acessing all global variables using 'global' keyword
	global string_name
	global int_emp_id
	global string_depart
	global string_desig
	global float_base_salary
	global float_gross_salary

	print(f'''
	------------------------------------------
	######### DISRUPT BRAND AGNECY ###########
	------------------------------------------
	[Employee Details]	:
	------------------------------------------
	1. Name 		:  {string_name}
	2. Employee Id		:  {int_emp_id}
	3. Department		:  {string_depart}
	4. Designation		:  {string_desig}
	5. Base Salary		:  {float_base_salary}
	6. Gross Salary		:  {float_gross_salary}
	------------------------------------------
	######### DISRUPT BRAND AGNECY ###########
	------------------------------------------
	 ''')

# Driver Code
setData()
getData()
 

