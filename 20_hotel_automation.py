# Printing The menu of Hotel

print("*************Welcome to Hotel Taj**************")


choice = True
exit = "Y"
bill = int(0)
item = int(0)   # initally bill is zero 
print('''
 ##################  HOTEL TAJ #####################
 * [FOOD DISHES]                   [RATE]          *
 * [1] Chicken Tandoori        :   240/plate       *
 * [2] Shahi Panneer           :   120/plate       *
 * [3] Ragda Patis             :   70/plate        *
 * [4] Chicken Biryani         :   180/plate       *
 * [5] Mutton Biryani          :   260/plate       *
 * [6] Shahi Chicken           :   180/plate       *
 * [7] Sparkling Water         :   40/glass        *
 * [99] No I'm good place my order                 *
 ##################################################
        ''')
   
while choice != False :
    while item != 99 :
        print("Enter the Item number you wish to order : ")
        item = int(input())
        if item > 0 and item < 99 :
           if item == 1 :
               bill = bill + int(240)
           if item == 2 :
               bill = bill + int(120)
           if item == 3 :
               bill = bill + int(70)
           if item == 4 :
               bill = bill + int(180)
           if item == 5 :
               bill = bill + int(260)
           if item == 6 :
               bill = bill + int(180)
           if item == 7 :
               bill = bill + int(40)
    print("Your Order is ready  :) ")
    print("Do you want to exit from menu : Y/N ?")
    exit = input()

    if exit == "y" or  exit == 'Y' :
        choice = False


print("Your bill before discount : ",bill)

if bill > 200 and bill< 500:
    bill = bill -( (bill*10)/100)
    print("Your Bill is " + str(bill))
if bill > 500 and bill < 1000 :
    bill = bill - ( (bill*15)/100)
    print("Your bill is "+ str(bill))
if bill > 1000 :
    bill = bill - ( (bill*20)/100)
    print("Your bill is "+ str(bill))


print("########### Thank you for comming ############")
