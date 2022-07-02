# import modules here
import pandas as pd

#define user-defined data base-here
dict_sample = {
        # creating the key-value : empty list to store data dynamically
        "name"          : [],
#        "item_name"     : [],
        "serial"        : [],
        "price"         : [],
        "qty"           : []
        }

#define function here 

# define function here

def putDataBaseDetails(items) : 
    global dict_sample
    for INDEX in range(0,items):
        print("Enter the name of Product[{INDEX+1}] ")
        dict_sample["name"].append(input(f"[+]Enter name of product       : "))
        dict_sample["serial"].append(int(input(f"[+]Enter the serial number : ")))
        dict_sample["price"].append(int(input(f"[+]Enter the price         : ")))
        dict_sample["qty"].append(int(input(f"[+]Enter the quantity of {dict_sample['name'][INDEX]} : ")))

def getDataBaseDetails(dict_sample):
    df = pd.DataFrame(dict_sample)
    print(df)



putDataBaseDetails(3)
getDataBaseDetails(dict_sample)
