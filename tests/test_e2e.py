from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_product_lifecycle():
    with open("tests/test_image.jpg", "rb") as image:

        create_response = client.post(
            "/products",
            data={
                "name": "Keyboard",
                "category": "Electronics",
                "price": 99.99
            },
            files={
                "image": ("test_image.jpg", image, "image/jpg")
            }
        )

    assert create_response.status_code == 200

    product = create_response.json()
    product_id = product["id"]

    list_response = client.get("/products")

    assert list_response.status_code == 200

    products = list_response.json()

    assert any(
        p["id"] == product_id
        for p in products
    )

    delete_response = client.delete(
        f"/products/{product_id}"
    )

    assert delete_response.status_code == 200

    final_list = client.get("/products").json()

    assert not any(
        p["id"] == product_id
        for p in final_list
    )
