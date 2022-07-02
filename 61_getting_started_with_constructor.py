# import modules here 

# definne class here 
class ABC : 
    class_var = 0

    def __init__(self,var):
        self.var        = var 
        ABC.class_var   += 1

        print(f"The value of object variable    :  {self.var}")
        print(f"The value of class variable     :  {ABC.class_var}")

object_01 = ABC(11)
object_02 = ABC(12)
object_03 = ABC(13)
object_04 = ABC(14)
object_05 = ABC(15)
object_06 = ABC(16)
