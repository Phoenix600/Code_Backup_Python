# function defination for each step-wise-problem

""" @countChar() to calulate the number of charcters in string"""
def countChar(str_message):
    return (len(str_message))

""" @printNtimes() to N-times string """
def printNTimes(str_message):
    n = int(input("[+]Enter number of times to repeat the string :"))
    print(str_message*n)

""" @print1stChar() to print 1st char of string """
def print1stChar(str_message):
    print(str_message[0])

""" @print1stThreeChar() to print first three charcters of string """
def print1stThreeChar(str_message):
    print(str_message[0:4])


def printLastThreeChar(str_message):
    print(str_message[-1:-4])


def print7thChar(str_message):
    if len(str_message) >= 7:
        print(str_message[6])
    else:
        print("The given string in not long enough :(")

def Upper(str_message):
    print(str_message.upper())


def ReplaceCharA(str_message):
    int_index = int(0)
    int_repIndx = int(0)
    int_end = int(len(str_message))-int(1)
    str_replace = "e"
    while  int_index != int_end :
        if str_message[int_index] == 'a':
            int_repIndx = int_index
            #str_temp = "e"
            str_message = str_replace
        int_index +=1


# Driver code
str_message = input("[+] Enter string message : ")
#ReplaceCharA(str_message)
print7thChar(str_message)
Upper(str_message)
print7thChar(str_message)
print1stThreeChar(str_message)

