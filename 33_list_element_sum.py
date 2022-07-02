# Import your modules here

def calSum(Sample_List) :
	sum = int(0)
	for size in range(0,len(Sample_List)):
		sum = sum + int(Sample_List[size])
	print("The sum of the series : ",sum)


# driver Code

List_Sample = [1,2,3,4,5,6,7,8,9]

calSum(List_Sample)
