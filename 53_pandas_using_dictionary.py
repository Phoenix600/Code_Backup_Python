# import modules here 
import pandas as pd

myBioData = {
        "Name"      :   "Pranay Ashok Ramteke",
        "Skills"    :   ["C/C++","Python","Graphic Designing","Ethical Hacking","App Developement"],
        "JobExp"    :   "Junior Designer At Disrupt Brand Ageny"
        }

myDataScienceVar = pd.DataFrame(myBioData)

print(myDataScienceVar)


print("Current Version of Pandas is ",pd.__version__)
