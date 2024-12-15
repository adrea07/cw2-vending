import socket
import json
import csv
from datetime import datetime

def handle_request(request):
    try:
        if request["action"] == "view_inventory":
            return handle_view_inventory()               #calls the function
        elif request["action"] == "add_cart":
            return handle_add_cart(request)              #calls the function
        else:
            #if action not identified, error
            return {"error"}
    except Exception as e:
        #processing error
        return {"error": str(e)}

def handle_view_inventory():
    try:
        with open('inventory.txt', 'r') as file:
            inventory = file.readlines()                        #reads all lines of inventory
        return {"status": "success", "data": inventory}
    except FileNotFoundError:
        return {"error": "Inventory file not found."}       #file not found error

def handle_add_cart(request):
    username = request["username"]              #catches name/other details from the request
    product_name = request["product"]
    quantity = int(request["quantity"])

    try:
        with open('inventory.txt', 'r') as file:
            lines = file.readlines()
        header = lines[0]
        products = [line.strip().split(',') for line in lines[1:]]          #product details

        product = next((p for p in products if p[1] == product_name), None)     #matches product to required product name
        if product:
            stock = int(product[3])     #stock available
            if quantity > stock:        #else....
                return {"error": "Insufficient stock."}

            product[3] = str(stock - quantity)
            with open('inventory.txt', 'w') as file:
                file.write(header)
                for p in products:
                    file.write(",".join(p) + "\n")          #update inventory

            cart_filename = f"{username}_cart.csv"
            with open(cart_filename, 'a', newline='') as file:          #create cart 
                writer = csv.writer(file)
                cost = float(product[2]) * quantity
                writer.writerow([product_name, quantity, f"{cost:.2f} AED"])

            with open('purchase_trends.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([product_name, quantity, datetime.now().strftime("%Y-%m-%d")])

            return {"status": "success", "message": f"{quantity} units of {product_name} added to your cart."}
        else:
            return {"error"}
    except Exception as e:
        return {"error": str(e)}

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #create socked object
    server_socket.bind(("127.0.0.1", 8081))                             #binding
    server_socket.listen(3)                 #listens for 3 connections
    print("Server started. Waiting for connections...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        data = client_socket.recv(1024).decode("utf-8")     #response recieved from client 
        request = json.loads(data)
        response = handle_request(request)
        client_socket.send(json.dumps(response).encode("utf-8"))   #response sent back to client
        client_socket.close()                       #close connection

if __name__ == "__main__":
    start_server()      #script execution
