import httpx

from ui.options import create_order, get_order_id


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


if __name__ == "__main__":
    send_order()
    get_order()