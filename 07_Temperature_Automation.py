#taking temperature from user in degree celcius : 
temp_celcius    = float(input("[+]Enter temprature in degree celcius : "))
temp_farhenite  = float((1.8*temp_celcius)+32)

## This willprint the cnverted temp

# Condition for the automation of FAN and AC
if temp_farhenite > 98 :
    print("Turn on AC")
elif temp_farhenite < 98 and temp_farhenite > 68 :
    print("Turn on Fan")
else :
    print("Turn off Fan and AC")
