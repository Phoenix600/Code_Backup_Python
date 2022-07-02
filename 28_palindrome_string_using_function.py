# GLobal variables 
string_01 = ""
string_02 = ""

'''
@isPalindrome() function to check whether the string is palindrome or not ,
 the given function will return bool variable
 '''

# By default every string is not palindrome string 
# base flag 
bool_var = False


def isPalindrome():
	'''
@isPalindrome() function to check whether the string is palindrome or not ,
 the given function will return bool variable
	 '''
#	(isPalindrome.__doctype__)


#	Accessing globbal variable using 'global' keyword 
	global string_01
	global string_02
	global bool_var
	# Taking input as string_01 
	string_01 = input("[+]Enter the string to check it is palindrome or nor : ")
	
	#asigning the reverse string_01 to string_02
	string_02 = string_01[::-1]

	# Comparsion for string is palindrome or not 
	if string_01 == string_02:
		bool_var = True
	else:
		bool_var = False



# Driver code 	

isPalindrome()

if bool_var == True:
	print("Palindrome")
else:
	print("Not palindrome")
