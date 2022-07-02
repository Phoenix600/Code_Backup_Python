bool_choice = True
char_grade = "NULL" # Taking grade initially as NULL or none
while bool_choice != False :
	print("############# CPS STUDENT SEVER ##################")

	print("[+]Enter the following details to display makrsheet")
	string_name   = input("[+]Name 		: ")
	int_roll_no   = int(input("[+]Roll			: "))
	int_year      = int(input("[+]Year			: "))
	string_depart = str(input("[+]Department		: "))
	int_semester  = int(input("[+]Semester		:"))
	# Taking marks of 5 subjects as input from student
	float_sub1    = float(input("[+]Marks of subject 1 	: "))
	float_sub2    = float(input("[+]Marks of subject 2	: "))
	float_sub3    = float(input("[+]Marks of subject 3	: "))
	float_sub4    = float(input("[+]Marks of subject 4	: "))
	float_sub5    = float(input("[+]Marks of subject 5	: "))

	# Calculating total sum 
	float_total   = float(float_sub1 + float_sub2 + float_sub3 + float_sub4 + float_sub5)
	# calculating percentage	
	float_percentage = float((float_total/500.0)*100)
	# Marks wise grade conditions :
	if float_percentage >= 85.0 and float_percentage <= 100.0 :
		char_grade = "A+"
	elif float_percentage >= 75.0 and float_percentage < 85.0 :
		char_grade = "A"
	elif float_percentage >= 60.0 and float_percentage < 75.0 :
		char_grade = "B"
	elif float_percentage >= 50.0 and float_percentage < 60.0 :
		char_grade = "C"
	elif float_percentage >= 40.0 and float_percentage < 50.0 :
		char_grade = "D"
	elif float_percentage < 40.0 :
		char_grade = "F"
	else :
		print("######Invalid grade#####")

	
	# Printing the marksheet of the student :
	print(f'''
	########### STUDENT PUBLIC SERVER ##############
	-------------------------------------------------
	# [{string_name}] Marksheet 
	-------------------------------------------------
   	 [Student Details]		
        -------------------------------------------------
         1 Name 		:   {string_name}
	 2.Roll			:   {int_roll_no}
	 3.Year			:   {int_year}
	 4.Department 		:   {string_depart}
	 5.Semester		:   {int_semester}
	-------------------------------------------------
   	 [Subject Wise Marks]
       	-------------------------------------------------
       	1.Signal Processing 	:   {float_sub1}
	2.EMF			:   {float_sub2}
	3.Eng. Mathematics 	:   {float_sub3}
	4.Python Prog		:   {float_sub4}
	5.Speaking Skills	:   {float_sub5}
        -------------------------------------------------
	 [Total] 		:   {float_total}
	 [Percentage]		:   {float_percentage}
	 [Garde]		:   {char_grade}
	------------------------------------------------
	''')

	flag =str(input("Do you want to print the marksheet of another student ? [Y] to print | [N] to Exit : "))
	if flag == "N" or flag == 'N':
		bool_choice = False
	else :
		bool_choice = True
