# defining FILE Handler 
FILE = open("data.txt","w")

FILE.write(input("[+] Enter your name        : ") + "\n")
FILE.write(input("[+] Enter Department       : ") + "\n")
FILE.write(input("[+] Enter your Year        : ") + "\n")
FILE.write(input("[+] Enter your Section     : ") + "\n")
FILE.write(input("[+] Enter your Roll        : ") + "\n")

# opening file in read-Mode to print the data 
FILE = open("data.txt",'r')
print(FILE.readlines())

FILE.close()
