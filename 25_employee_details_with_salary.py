#defining all global variables here

# basic Employee details 
string_name = ""
int_emp_id = int(0)
string_depart = ""
string_desig = ""

# EMployee gross salary details 
float_base_sal   = float(0)
float_HRA        = float(0)
float_TA         = float(0)
float_DA         = float(0)
float_inscentive = float(0)
float_PF         = float(0)
float_TDS        = float(0)
float_gross_sal  = float(0)

# @functions definations 

def getEmpDetails() :
	"""
	@getEmpDetails() to get basic info of employee
	Accessing global variables via 'global' keyword """
	# Taking input as basic Employee details 
	# basic Employee details 
	global string_name
	global int_emp_id
	global string_depart
	global string_desig
	
	print("=====================================")
	print("#	Employee Open Server 	    #")
	print("=====================================")
	print("[+]Enter the following detials 	: ")
	string_name = input("[+]Name			: ")
	int_emp_id = int(input("[+]Employee ID 		: "))
	string_depart = input("[+]Department		: ")
	string_design = input("[+]Designation		: ")
	

def getSalary() :
	"""@getSalary() to get the basic salary details of employee  """
	# Basic Salary details 
	global float_base_sal   
	global float_HRA        
	global float_TA         
	global float_DA         
	global float_inscentive 
	global float_PF         
	global float_TDS        
	global float_gross_sal 

	# Taking basic salary and other details via user 
	#print("[+]Enter the following details 		:")
	float_base_sal 		= float(input("[+]Base Salary		: "))
	float_HRA      		= float(input("[+]HRA			: "))/float(100.0)
	float_TA       		= float(input("[+]TA			: "))/float(100.0)
	float_DA       		= float(input("[+]DA			: "))/float(100.0)
	float_inscentive	= float(input("[+]Inscentive		: "))
	float_PF		= float(input("[+]PF			: "))
	float_TDS		= float(input("[+]TDS			: "))

	#calculating Gross Salary

	float_gross_sal = float(float_base_sal + float_HRA*float_base_sal + float_TA*float_base_sal + float_DA*float_base_sal + float(float_inscentive) - float(float_PF) - float(float_TDS))


	#	print(float_HRA)
	#	print(float_TA)
	#	print(float_DA)

def printSal() :
	print(f''' 
=====================================
#	Employee Open Server 	    #
=====================================
[Employee Detals] :
-------------------------------------
1. Name			: {string_name} 
2. Employee Id		: {int_emp_id}
3. Department		: {string_depart}
4. Designation		: {string_desig}
-------------------------------------
[Salary Details]  :
-------------------------------------
Base Salary		: {float_base_sal}
HRA			: {float_HRA} of BS
TA			: {float_TA} of BS
DA			: {float_DA} of BS
Incentive		: {float_inscentive}
PF			: -{float_PF}
TDS			: -{float_TDS}
-------------------------------------
Gross Salary		: {float_gross_sal}
--------------------------------------	
		
	''')


# main function to run all above processes 
def runCode():
	bool_choice = True
	int_key = int(0)
	while bool_choice != False :
		print(f'''
===================================================
############### DISRUPT BRAND AGENCY ###############
====================================================
[+]Select the following options		:
====================================================
[KEY]			[FUNCTION]
[ 1 ]			Fill Basic Employee Details
[ 2 ]			Fill Employee Salary Details
[ 3 ]			Get Gross Salary Certificate
[ 0 ]			EXIT
====================================================
[ + ] Enter the key to select specific options   :
		 ''')
		int_key = int(input())
		if int_key == 1 :
			getEmpDetails()
		elif int_key == 2:
			getSalary()
		elif int_key == 3:
			printSal() 
			bool_choice = False
		else :
			bool_choice = False
	
# Driver Code Area 

runCode()
