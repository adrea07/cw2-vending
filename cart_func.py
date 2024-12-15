import csv
from tkinter import *
import ttkbootstrap as tb
from tabulate import tabulate

class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = float(price)
        self.stock = int(stock)

    def reduce_stock(self, quantity):
        if quantity > self.stock:
            raise ValueError("Insufficient stock.")
        self.stock -= quantity

    def __str__(self):
        return f"{self.product_id},{self.name},{self.price},{self.stock}"
    
# def view_inventory():
#     with open('inventory.txt', 'r') as file:
#         lines = file.readlines()
#     header = lines[0]
#     inventory = []
#     print("ID, PRODUCT, PRICE, QTY\n")

#     for line in lines[1:]:
#         item_detail = line.strip().split(',')
#         print(", ".join(item_detail))

def create_cart(username):
    filename = f"{username}_cart.csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        header = ['Product Name', 'Quantity', 'Cost']
        writer.writerow(header)
    print(f"Cart created for {username}.")

# def add_cart(username):
#     filename = f"{username}_cart.csv"

#     # Load inventory
#     with open('inventory.txt', 'r') as file:
#         lines = file.readlines()
#     header = lines[0]
#     inventory = [Product(*line.strip().split(',')) for line in lines[1:]]

#     def show_selected():
#         selected_options = [option for option, var in check_vars.items() if var.get() == 1]

#         for selected in selected_options:
#             selected_name = selected.split(" - ")[0]
#             product = next((p for p in inventory if p.name == selected_name), None)

#             if product:
#                 try:
#                     qty = int(input(f"Enter quantity of {product.name} to add to cart: "))
#                     product.reduce_stock(qty)
#                     cost = product.price * qty  # Calculate the cost

#                     # Write to the cart
#                     with open(filename, 'a', newline='') as cart_file:
#                         cart_writer = csv.writer(cart_file)
#                         cart_writer.writerow([product.name, qty, f"{cost:.2f} AED"])
#                     print(f"\n{qty} units of {product.name} added to your cart! Total cost: {cost:.2f} AED\n")
#                 except ValueError as e:
#                     print(e)

#         # Update inventory file
#         with open('inventory.txt', 'w') as file:
#             file.write(header)
#             for product in inventory:
#                 file.write(str(product) + '\n')

#     # GUI for product selection
#     root = tb.Window(themename="superhero")
#     root.geometry('500x850')
#     root.title("INVENTORY")

#     check_vars = {}
#     options = [f"{product.name} - {product.price} AED" for product in inventory]

#     for option in options:
#         var = IntVar()
#         check_vars[option] = var
#         tb.Checkbutton(
#             root,
#             text=option,
#             variable=var,
#             padding=5,
#             bootstyle="info"
#         ).pack(anchor='w', padx=10, pady=5)

#     tb.Button(
#         root,
#         text="Add Selected to Cart",
#         command=show_selected,
#         bootstyle="success",
#         width=20,
#         padding=(10, 5)
#     ).pack(pady=30)

#     root.mainloop()



def view_cart(username):
    filename = f"{username}_cart.csv"
    total_cost = 0.0
    cart_items = [] 
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            print("\n*** YOUR CART ***")
            header = next(reader)  
            cart_items.append(header)  
            for i in reader:
                cart_items.append(i)  
                total_cost += float(i[2].split()[0])  
    except FileNotFoundError:
        print("Empty Cart, Please add items first! ")
        return 0

    print(tabulate(cart_items, headers='firstrow', tablefmt='grid'))

    print(f"\nTotal Amount = {total_cost:.2f} AED")
    return total_cost




