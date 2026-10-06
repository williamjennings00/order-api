import httpx

from ui.options import create_order


def send_order():
    order = create_order()

    response = httpx.post(
        "http://127.0.0.1:8000/orders",
        json=order
    )

    print(response.json())


if __name__ == "__main__":
    send_order()