def menu_Print():
    print(
'''   
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

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

***********************************
** What would you like to order? **
***********************************
'''
)
menu_Print()

menu_Dict = {
"Cookies": 0,
"Spring Rolls": 0,
"Salmon": 0,
"Steak": 0 ,
"Meat Tornado": 0,
"A Literal Garden": 0,
"Ice Cream": 0,
"Cake": 0,
"Pie": 0,
"Coffee": 0,
"Tea": 0,
"Unicorn Tears": 0
}

order_input = input("> ")

while order_input != "quit":
    if order_input in menu_Dict:
       menu_Dict[order_input] += 1  
    print(f"** {menu_Dict.get(order_input)} one order of {order_input} has been added to your meal **")
    order_input = input("> ")
else: 
    print("quit")
    



##Create dict
##Add items to the dict
##Check if the requested item is already there 
##Break from the loop if input = quit