import httpx

from ui.options import create_order, get_order_to_update


def send_order():
    order = create_order()

    response = httpx.post(
        "http://127.0.0.1:8000/orders",
        json=order
    )

    print(response.json())

def get_order():
    order_id = input("Enter order ID: ")

    response = httpx.get(
        f"http://127.0.0.1:8000/orders/{order_id}"
    )

    print("Status:", response.status_code)
    print("Response:", response.text)

def get_all_orders():

    response = httpx.get(
        f"http://127.0.0.1:8000/orders"
    )
    print("Status:", response.status_code)
    print("Response:", response.text)

def update_order():
    order_id, new_status = get_order_to_update()

    response = httpx.patch(
        f"http://127.0.0.1:8000/orders/{order_id}",
        json={
            "status": new_status
        }
    )

    print("Status:", response.status_code)
    print("Response:", response.text)

if __name__ == "__main__":
    send_order()
    get_order()
    get_all_orders()
    update_order()
    get_all_orders()