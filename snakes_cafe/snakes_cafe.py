print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
""")

print("""
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
""")

print("""
***********************************
** What would you like to order? **
***********************************
""")



menu={'Wings':0,'Cookies':0,'Spring Rolls':0,'Salmon':0 ,'Steak':0,'Meat Tornado':0,'A Literal Garden':0,'Ice Cream':0,'Cake':0,'Pie':0,'Coffee':0,'Tea':0,'Unicorn_Tears':0}

def snakes_cafe():
    order=0
    while (order!="quit"):
        order= input(">")
        for x in menu :
            if order == x :
                menu[order]+=1
                print(f"** {menu[order]} order of {x} have been added to your meal **")
                break
        else:
            print("sorry this order not found in meal")
                       
 
snakes_cafe()  
      








