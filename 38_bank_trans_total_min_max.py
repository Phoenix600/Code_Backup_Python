# Global Variables
float_total_amt = float(0)
float_min_amt = float(9999999)
float_max_amt = float(0)
tuple_transaction = (10000,5000,2000,15000,500,450,200,20000)

# all essential function/procedures are defined here

def getMin():
	''' @getMin() function will give the minimum tarnsaction amount '''
	
	# Acessing global variable 
	global tuple_transaction
	global float_min_amt

	# Finding the minimum transaction 
	for COUNT in range(0,len(tuple_transaction)):
		if float_min_amt > tuple_transaction[COUNT]:
			float_min_amt = tuple_transaction[COUNT]

def getMax():
	''' @getMax function will give the maximum transaction amount '''
	# Acessing the global variable 
	global tuple_transaction 
	global float_max_amt

	#Finding the maximum transaction 
	for COUNT in range(0,len(tuple_transaction)):
		if float_max_amt < tuple_transaction[COUNT]:
			float_max_amt = tuple_transaction[COUNT]

def getTotal():
	'''@getTotal function will give the total ammount of transaction'''
	
	# Accessing the global variable
	global tuple_transaction
	global float_total_amt
	
	for COUNT in range(0,len(tuple_transaction)):
		float_total_amt += float(tuple_transaction[COUNT])


def TransDetails():
	getMin()
	getMax()
	getTotal()

	print(f'''
	Minimum Transaction ammount  : {float_min_amt}
	Maximum Transaction ammount  : {float_max_amt}
	Total Transaction amount     : {float_total_amt} 
 	''')


TransDetails()
	
