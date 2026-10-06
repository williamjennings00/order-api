from datetime import datetime
# * Create an order
# * Get one order
# * Get all orders
# * Update an order
# * Delete an order
# * Filter orders by status


from datetime import datetime


VALID_STATUSES = {"pending", "processing", "shipped", "cancelled"}


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


def create_order():
    while True:
        order = {
            "id": input("Enter ID: ").strip(),
            "customer_name": input("Enter customer name: ").strip(),
            "product": input("Enter product: ").strip(),
            "quantity": get_quantity(),
            "price": get_price(),
            "status": get_status(),
            "created_at": datetime.now()
        }

        print()
        print(order)

        confirmation = input(
            "Is your order correct? (yes/no): "
        ).strip().lower()

        if confirmation == "yes":
            return order

        print("\nLet's enter the order again.\n")