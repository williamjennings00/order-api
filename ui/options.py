from datetime import datetime


VALID_STATUSES = {"pending", "processing", "shipped", "cancelled"}


def get_required_input(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")


def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                return quantity

            print("Quantity must be greater than 0.")

        except ValueError:
            print("Enter a valid whole number.")


def get_price():
    while True:
        try:
            price = float(input("Enter price: "))

            if price >= 0:
                return price

            print("Price cannot be negative.")

        except ValueError:
            print("Enter a valid price.")


def get_status():
    while True:
        status = input(
            "Enter status (pending, processing, shipped, cancelled): "
        ).strip().lower()

        if status in VALID_STATUSES:
            return status

        print("Invalid status.")


def confirm_order():
    while True:
        confirmation = input(
            "Is your order correct? (yes/no): "
        ).strip().lower()

        if confirmation == "yes":
            return True

        if confirmation == "no":
            return False

        print("Enter yes or no.")


def create_order():
    while True:
        order = {
            "customer_name": get_required_input("Enter customer name: "),
            "product": get_required_input("Enter product: "),
            "quantity": get_quantity(),
            "price": get_price(),
            "status": get_status(),
        }

        print()
        print(order)
        print()

        if confirm_order():
            return order

        print("\nLet's enter the order again.\n")

def confirm_get_order():
    while True:
        confirmation = input(
            "Is the order ID you want to retrieve correct? (yes/no): "
        ).strip().lower()

        if confirmation == "yes":
            return True

        if confirmation == "no":
            return False

        print("Enter yes or no.")

def get_order_id():
    while True:
        order_id = get_required_input("Enter order ID: ")

        print()
        print(order_id)
        print()

        if confirm_get_order():
            return
        print("\nLet's enter the order ID again.\n")