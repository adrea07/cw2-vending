from tkinter import *
import ttkbootstrap as tb
from datetime import datetime, timedelta
import random
from userdetails import read_user


def payment(user_type):
    def button_func():
        if selected_payment.get() == "None":
            result_label.config(text="Please select a payment option.")
        elif selected_payment.get() == "Cash":
            handle_cash_payment()
        elif selected_payment.get() == "Card":
            handle_card_payment()

    def handle_cash_payment():
        if user_type == "guest":
            address = input("Please enter your delivery address: ")
        else:
            username = input("Please enter your username again: ")
            address = read_user(username)

        delivery_date = datetime.now() + timedelta(days=random.randint(1, 7))
        print(f"\nThank you! Your order will be delivered to:\n{address}")
        print(f"Estimated delivery date: {delivery_date.strftime('%A, %d %B %Y')}.")

    def handle_card_payment():
        def process_payment():
            card_number = card_entry.get()
            cvc = cvc_entry.get()
            if len(card_number) == 16 and card_number.isdigit() and len(cvc) == 3 and cvc.isdigit():
                result_label.config(text="Payment successful!")
                print("Your purchase will be sent via mail!!\n")
            else:
                result_label.config(text="Invalid card details. Please try again.")

        # Create a new window for card payment
        card_root = tb.Window(themename="superhero")
        card_root.geometry("550x550")
        card_root.title("Card Payment")

        frame = Frame(card_root)
        frame.pack(pady=20)

        Label(frame, text="Enter Card Details", font=("Arial", 12, "bold")).pack(pady=10)

        Label(frame, text="Card Number:").pack(anchor="w")
        card_entry = Entry(frame, width=30)
        card_entry.pack(pady=5)

        Label(frame, text="CVC:").pack(anchor="w")
        cvc_entry = Entry(frame, width=10, show="*")
        cvc_entry.pack(pady=5)

        # Local result_label for feedback
        result_label = Label(frame, text="", font=("Arial", 10))
        result_label.pack(pady=10)

        Button(frame, text="Submit Payment", command=process_payment).pack(pady=10)

        card_root.mainloop()


    # Main GUI for Payment Options
    root = tb.Window(themename="superhero")
    root.geometry('500x350')
    root.title('PAYMENT')

    frame = Frame(root)
    frame.pack()

    heading_label = Label(frame, text="Payment Options:", font=("Arial", 12, "bold"))
    heading_label.pack(anchor="w", pady=5, padx=10)

    selected_payment = StringVar(value="None")

    Rbtn1 = Radiobutton(frame, text="Card Payment", width=15, font=("Helvetica", 12), variable=selected_payment, value="Card")
    Rbtn1.pack(padx=5, pady=5)

    Rbtn2 = Radiobutton(frame, text="Cash on Delivery", width=15, font=("Helvetica", 12), variable=selected_payment, value="Cash")
    Rbtn2.pack(padx=5, pady=5)

    proceed_button = Button(frame, text="Proceed", bg="light gray", relief=RAISED, command=button_func)
    proceed_button.pack(pady=10)

    result_label = Label(frame, anchor="w", wraplength=280, justify="left")
    result_label.pack(fill="x", padx=10, pady=5)

    root.mainloop()
