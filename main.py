#importing functions from files/ functions from libraries
from cart_func import view_cart, create_cart
from client import add_cart, plot_purchase_trends, view_inventory_client
from userdetails import existing_user, user_details
from tkinter import *
import ttkbootstrap as tb

username = ''
# Main menu loop

print("Welcome to the T-LI SMART VENDING MACHINE\n")
while True:
    print('1. Enter as guest')
    print('2. Login/create an account')
    print('3. Exit the SMART VENDING MACHINE')

    x = int(input('enter choice: '))

    if x == 1:
        username = input('enter your name: ')
        user_type = 'guest'
                            #store user_type for further use
        create_cart(username) 
                             #creates a guestname.csv cart specific for each user
        print(f"\nWelcome {username}!!")
        break  
    if x == 2:
        #registered users
        print('1. login to existing account')
        print('2. Create a new account')
        print('3. exit')

        y = int(input('enter choice: '))

        if y == 1:
            user_type = 'not guest'
                                    #useful for further use
            user = existing_user()
                                    #gets username from LOGIN database
            create_cart(user) 
                                    #creates cart for user
            break
        elif y == 2:
            user_type = 'not guest'
            username = user_details()
            create_cart(username)  
            #username.csv cart
            break
        elif y == 3:
            break
    elif x == 3:
        print('BYE, do visit us again!')
        break

# Shopping menu loop
while True:
    print('1. View all items in the machine')
    print('2. Add item to cart')
    print('3. View cart')
    print('4. View Purchase Trends Graph')
    print('5. Exit')

    x = int(input('Enter choice: '))

    if x == 1:
        view_inventory_client()       #views all items from inventory.txt
    elif x == 2:
        add_cart(username)      #proceeds to gui and selection if items
    elif x == 3:
        view_cart(username)             #view cart function
        print('1. Continue shopping')
        print('2. Proceed to payment')

        y = int(input('Enter choice: '))

        if y == 1:
            print("Continuing your shopping...")
        elif y == 2:
            print("Proceeding to payment...\n")
            from transaction import payment         #transaction starts
            payment(user_type)                              #registers user_type for purposes like delivery address
            print("THANK YOU FOR SHOPPING WITH US\n")
            print("WE LOOK FORWARD TO SEEING YOU AGAIN:)")
            break
    elif x == 4:
        plot_purchase_trends()

    elif x == 5:
        print("Thank you for visiting!")    #exits loop/leave the smart vending machine
        break







#         if y == 1:
#             user_type = 'not guest'
#             existing_user()
#             break 
#         elif y == 2:
#             user_type = 'not guest'
#             user_details()
#             break  
#         elif y == 3:
#             break

#     if x == 3:
#         print('BYE, do visit us again!')
#         break  

# # Shopping menu loop
# while True:
#     print('1. View all items in the machine')
#     print('2. Add item to cart')
#     print('3. View cart')
#     print('4. Exit')

#     x = int(input('enter choice: '))

#     if x == 1:
#         view_inventory()
#         continue  

#     if x == 2:
#         add_cart()
#         continue  

#     if x == 3:
#         view_cart()
#         print('1. Continue shopping')
#         print('2. Proceed to payment')

#         y = int(input('enter choice: '))

#         if y == 1:
#             print("Continuing your shopping...")
#             continue 
#         elif y == 2:
#             print("Proceeding to payment...\n")
#             from transaction import payment
#             payment(user_type)


            

