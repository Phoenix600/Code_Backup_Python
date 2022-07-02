float_temp = float(input("Enter the temperature : "))

bool_flag = False;

if(float_temp < -273 or float_temp == -273 or (float_temp > -273 and float_temp < 0)) :
    print("Invalid temperature")
