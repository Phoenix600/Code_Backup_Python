# Setting range
int_range = int(input("[+]Enter the number of terms : "))
# Acting as indexing for odd num series 
int_num = 0

for odd_num in range(int_range):
    print((2*int_num-1)**2)
    int_num += 1


