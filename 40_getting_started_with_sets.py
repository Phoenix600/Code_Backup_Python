# import your modules here

# define global variables here

# define functions here

# Write main driver code here 

'''predefined data base in the form of sets{} '''
developers = {'Pranay','Diya','Vedant','Shubham'}
analyist = {'Pranay','Mayur','Siddhesh','Diya'}

allEmployees   		= developers.union(analyist)
devANDanalyist 		= developers.intersection(analyist)
developersOnly 		= developers.difference(analyist)
analiystOnly   		= analyist.difference(developers)     
DevOnlyANDanalyistOnly  = developers ^ analyist

'''or
There is shortHand '^' for symmetric_difference 
DevOnlyANDanalyistOnly  = developers.symmetric_differnce(analyist)
 '''

print(f'[+] Total Number of employees in company		: {len(allEmployees)}')
print(f'[+] List  of employees in company			: {allEmployees}')
print(f'[+] List of Developers in company              		 : {developers}')
print(f'[+] List of Analyist in company 	       		 : {analyist}')
print(f'[+] List of employee which Devs and Analiyst		 : {devANDanalyist}')
print(f'[+] List of emp which are only dev and only analyist	 : {DevOnlyANDanalyistOnly} ')



