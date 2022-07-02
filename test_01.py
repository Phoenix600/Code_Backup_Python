FILE = open("info.txt","r")

upper = int(0)
lower = int(0)

text = FILE.read()

for char in text :
    if char.isupper():
        upper+=1
    else:
        lower+=1


print(upper)
print(lower)

