from datetime import datetime
# * Create an order
# * Get one order
# * Get all orders
# * Update an order
# * Delete an order
# * Filter orders by status


def create_order():
    valid_statuses = {"pending", "processing", "shipped", "cancelled"}

    while True:
        order_id = input("Enter ID: ").strip()
        customer_name = input("Enter customer name: ").strip()
        product = input("Enter product: ").strip()

        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    break

                print("Quantity must be greater than 0.")

            except ValueError:
                print("Enter a valid whole number.")

        while True:
            try:
                price = float(input("Enter price: "))

                if price >= 0:
                    break

                print("Price cannot be negative.")

            except ValueError:
                print("Enter a valid price.")

        while True:
            status = input(
                "Enter status (pending, processing, shipped, cancelled): "
            ).strip().lower()

            if status in valid_statuses:
                break

            print("Invalid status.")

        order = {
            "id": order_id,
            "customer_name": customer_name,
            "product": product,
            "quantity": quantity,
            "price": price,
            "status": status,
            "created_at": datetime.now()
        }

        print()
        print(order)

        confirmation = input("Is your order correct? (yes/no): ").strip().lower()

        if confirmation == "yes":
            return order

        print("\nLet's enter the order again.\n")