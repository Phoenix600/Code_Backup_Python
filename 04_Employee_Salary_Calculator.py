# Inputs Name Basic_Salary DA = 0.9 * BS   HRA = 0.4*BS  TA = 0.3*BS

print(" ********* Employee Salary Details *********")
string_name = input("[+]Name           : ")
int_Salary  = int(input("[+]Enter Basic Salary : "))  


### Cacluating other Constraints 
string_DA  = str(0.9*int_Salary)
string_HRA = str(0.4*int_Salary)
string_TA  = str(0.3*int_Salary)

### Printing Output
print(" ********* "+ string_name +" Salary Details *********")
print(int_Salary)
print(string_DA)
print(string_HRA)
print(string_TA)

