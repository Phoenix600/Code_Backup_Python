# Printing the details of the student

#   1.Name   2. Year  3. Section  4. Roll Number  5. Age  6. EmailId 7. Contact number

print("*****************ENTER YOUR DETAILS********************")

string_name  = input("[+]Name        : ")
int_year     = input("[+]Year        : ")
char_section = input("[+]Section     : ")
int_roll_no  = input("[+]Roll Number : ")
int_age      = input("[+]Age         : ")
string_Email = input("[+]Email Id    : ")
string_phone = str(input("[+]Phone No    : "))    


# Printing Output 
print("\n")
print("*****************HERE ARE YOUR DETAILS********************")
print("[+]Name        : ",string_name)
print("[+]Year        : ",int_year)
print("[+]Section     : ",char_section)
print("[+]Roll Number : ",int_roll_no)
print("[+]Age         : ",int_age)
print("[+]Email Id    : ",string_Email)
print("[+]Phone No    : ",string_phone)
