# Setting stocks of the inventory items to 10/10 [IN STOCK] 

int_spark_plug = int(3)
int_abs        = int(3)
int_carborator = int(3)
## <----------Add more inventory items here with their qty ----------------->


## <-----------Keeping Track of Bill ----------------->
int_bill = int(0)


## <----------Keeping Track of Order ---------------------->
int_order = int(0)

###  MENU

bool_choice = True
 
while bool_choice != False:
    print(f'''
        #############################################################
        #          DAVID'S INVENTORY AUTOMOBILE  SHOP               #
        #############################################################
        [SN]    [INVENTORY NAME]        [PRICE]          [INSTOCK]
         1.     Spark Plug              300                 {int_spark_plug}
         2.     ABS Brakes              1800                {int_abs}
         3.     Carborator              5000                {int_carborator}
        99.     [PLACE MY ORDER]
         ''')  
    int_order = int(input("[+]Select item number to buy : "))
    if int_order == 1 :
        if int_spark_plug == 0 :
            print("############[CAUTION] : Spark Plug is out of stock :( ")
        else :
            int_bill = int_bill + 300
            int_spark_plug-= 1
    elif int_order == 2:
        if int_abs == 0:
            print("############[CAUTION] : ABS Brakes is out of stock :( ")
        else:
            int_bill = int_bill + 1800
            int_abs-=1
 
    elif int_order == 3:
        if int_carborator == 0 :
            print("############[CAUTION] : Carborator is out of stock :( ")
        else:
            int_bill = int_bill + 5000
            int_carborator-=1
    elif int_order == 99:
        print('''
        ################################################################
        #------------------YOUR ORDER HAS BEEN PLACED------------------#
        ################################################################
                ''')
        bool_choice = False
    else :
        print("Invalid Output")

#print(f"Your total bill  : {int_bill} ")

if int_bill < 5000 :
    gst = (int_bill*15/100)
    delTax = 200
    SBA    = 10
    GETAX  = 10
    print(f'''
    ##########BILL RECIPT ##########
    Cost             :   {int_bill}
    GST of 15%       :   {gst}
    Delivery Tax     :   {delTax}
    Girl Edu Tax     :   {GETAX}
    SBA TAX          :   {SBA}
    ------------------------------
    TOTAL            :   {int_bill + gst + delTax + GETAX + SBA}
    ''')
else :
    gst = (int_bill*22.22/100)
    delTax = 200
    SBA    = 10
    GETAX  = 10
    print(f'''
    ##########BILL RECIPT ##########
    Cost             :   {int_bill}
    GST of 22.22     :   {gst}
    Delivery Tax     :   {delTax}
    Girl Edu Tax     :   {GETAX}
    SBA TAX          :   {SBA}
    ------------------------------
    TOTAL            :   {int_bill + gst + delTax + GETAX + SBA}
    ''')

