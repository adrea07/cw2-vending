import socket
import json
import csv
import matplotlib.pyplot as plt
from tkinter import *
import ttkbootstrap as tb

def send_request_to_server(request):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("127.0.0.1", 8081))
        client_socket.send(json.dumps(request).encode("utf-8"))
        response_data = client_socket.recv(1024).decode("utf-8")
        return json.loads(response_data)
    except ConnectionError:
        return {"status": "error", "message": "Could not connect to server."}
    finally:
        client_socket.close()

def view_inventory_client():
    # Create the request dictionary
    request = {"action": "view_inventory"}
    
    # Send the request to the server
    response = send_request_to_server(request)
    
    if response.get("status") == "success":
        print("ID, PRODUCT, PRICE, QTY\n")
        for line in response["data"]:
            print(line.strip())  # Display each inventory line
    else:
        print("Error viewing inventory:", response.get("error", "Unknown error"))


def add_cart(username):
    request = {"action": "view_inventory"}
    response = send_request_to_server(request)

    if response["status"] != "success":
        print("Error fetching inventory:", response["message"])
        return

    inventory = response["data"]
    products = [item.split(",") for item in inventory[1:]]  # Skip header

    root = tb.Window(themename="superhero")
    root.geometry('500x850')
    root.title("INVENTORY")

    check_vars = {}
    options = [f"{product[1]} - {product[2]} AED" for product in products]  # Display name and price

    def show_selected():
        selected_options = [option for option, var in check_vars.items() if var.get() == 1]

        for selected in selected_options:
            selected_name = selected.split(" - ")[0]
            product = next((p for p in products if p[1] == selected_name), None)

            if product:
                try:
                    qty = int(input(f"Enter quantity of {product[1]} to add to cart: "))
                    request = {
                        "action": "add_cart",
                        "username": username,
                        "product": product[1],
                        "quantity": qty
                    }
                    cart_response = send_request_to_server(request)
                    print(cart_response["message"])
                except ValueError as e:
                    print("Invalid quantity:", e)

    for option in options:
        var = IntVar()
        check_vars[option] = var
        tb.Checkbutton(
            root,
            text=option,
            variable=var,
            padding=5,
            bootstyle="info"
        ).pack(anchor='w', padx=10, pady=5)

    tb.Button(
        root,
        text="Add Selected to Cart",
        command=show_selected,
        bootstyle="success",
        width=20,
        padding=(10, 5)
    ).pack(pady=30)

    root.mainloop()

def plot_purchase_trends():
    purchase_data = {}          # Read purchase data from CSV file created in server
    try:
        with open('purchase_trends.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                product_name = row[0]
                quantity = int(row[1])
                purchase_data[product_name] = purchase_data.get(product_name, 0) + quantity
    except FileNotFoundError:
        print("Purchase data file not found.")
        return
    
    products = list(purchase_data.keys())
    quantities = list(purchase_data.values())        # data for bar chart

    # Creating the chart
    plt.figure(figsize=(10, 6))
    plt.bar(products, quantities, color='skyblue')
    plt.xlabel('Product Name')
    plt.ylabel('Total Quantity Purchased')
    plt.title('Purchase Trends')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

plot_purchase_trends()
