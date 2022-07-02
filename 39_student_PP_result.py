# Global Tuple 
tuple_PP_marks = (40,39,16,18,5,40,37,38)

# Global variable are defined here
float_high_marks = float(0)
float_PP_result = float(0)
float_pass_criteria = float(max(tuple_PP_marks)/2.0)
int_stud_passed = int(0)
float_class_result = float(0)

# Fucntion defined here

def getMaxMarks():
	# Accessing global variable 
	global float_high_marks 
	global tuple_PP_marks
	global float_pass_criteria

	# calculating the maximum marks 
	for INDEX in range(0,len(tuple_PP_marks)):
		if float_high_marks < tuple_PP_marks[INDEX] :
			float_high_marks = tuple_PP_marks[INDEX]
		else :
			pass


def getPassStud():
	# Accessing global variable
	global tuple_PP_marks
	global float_pass_criteria
	global int_stud_passed
	
	for INDEX in range(0,len(tuple_PP_marks)):
		if tuple_PP_marks[INDEX] >= float_pass_criteria :
			int_stud_passed+=1

def getPercentage() :
	
	global tuple_PP_marks
	global int_stud_passed
	global float_class_result
	
	float_class_result = float((int_stud_passed/ len(tuple_PP_marks)) * 100.0)
	

def getData() : 
	
	global float_high_marks
	global float_PP_result 
	global float_pass_criteria
	global int_stud_passed
	global float_class_result
	global tuple_PP_marks

	print(f'''
	+---------------------------------------------+
		Python Programming Result
	+---------------------------------------------+
	[01] Highest Marks 	: {float_high_marks}
	[02] Passed Students    : {int_stud_passed}
	[03] Total Students 	: {len(tuple_PP_marks)}
	[04] % of Passed studet : {float_class_result}
	+---------------------------------------------+
	 ''')



def runCode():
	getMaxMarks()
	getPassStud()
	getPercentage()
	getData()

# driver code

runCode()
