# creating the FILE handler or FILE object 
import subprocess as sp

sp.call("ls  | grep .txt",shell=True)
print("These are available orignal files : ")
with open(input("[+]Enter the existing file name to open : "),"r") as FILE0 :
    copyData = FILE0.read()

with open(input("[+]Enter new file name to copy Data : "),"w") as FILE1 :
    FILE1.write(copyData)

FILE0.close()
FILE1.close()

