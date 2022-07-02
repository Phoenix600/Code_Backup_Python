# Defining File Handler 
FILE = open("data.txt","r")

vowels      = int(0)
consonent   = int(0)

line1 = FILE.readline()

print("The content of the whole line is \n")
print(line1)

for char in line1 :
    if char in 'aeiou' :
        vowels+=1
    else:
        consonent+=1

print(f"[+]Number of consonets {consonent}")
print(f"[+]Number of Vowels {vowels}")


