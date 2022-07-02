# Getting data from the user

start_point = int(input("(+)Enter the first term :"))
#n =int( input(f"(+)Enter How Many Terms You Want To Display after{start_point} : "))
end_point = int(input("(+)Enter the last term :"))
n = 1;
for odd_num in range(start_point, end_point, (2*n-1) ):
    #print(2*n-1)
    print(start_point)
    start_point+=1

