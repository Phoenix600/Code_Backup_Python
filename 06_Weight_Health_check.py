#Getting weight from the user in kg
float_weight = (float)(input("[+]Enter your weight in KG : "))
float_pounds = (float)(float_weight*2.2)

#Printing the weight in pounds
print("[+]Your Weight in Pounds : ",float_pounds)

# Condition to check wether the person has appropriate weight or not 
# if <condition> :
#        statement
# else :
#        statement

if float_pounds < 120 :
    print("[+]You are under weight")
else :
    print("[+]Your weight is approriate")
