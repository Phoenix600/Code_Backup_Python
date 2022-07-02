# Taking number of terms from the user

int_size = int(input("Enter the numbr of terms : "))
if int_size >= 0 :
    print("General series of [(num**3)-1] is : ")
for series in range (1,int_size):
    print(((series)**3)-1, end ="\t ")
    print("\n")
else :
    print("Invalid input")
