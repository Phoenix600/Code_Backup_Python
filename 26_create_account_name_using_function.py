#Import your modules here 


str_Fname = ""
str_Lname = ""
str_AccName =""

def createAccount(str_Acc_Name):
    global str_Fname
    global str_Lname
    global str_AccName

    str_Fname = input("[+]Enter first name : ")
    str_Lname = input("[+]Enter last name : ")

    for indx in range(0,3):
        str_AccName[indx] = str_AccName + str_Fname[indx]

    indx = len(str_Accname)

    for count in range(0,3):
        str_AccName[indx + count + 1] = str_AccName + str_Lname[count]


createAccount()
