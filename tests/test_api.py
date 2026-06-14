from fastapi.testclient import TestClient

from app.main import app

# ========================
# Interation Tests (HTTPx)


client = TestClient(app)

def test_create_product_success():
    with open("tests/test_image.jpg", "rb") as image:
        response = client.post(
            "/products",
            data={
                "name": "Mouse",
                "category": "Electronics",
                "price": "99.90"
            },
            files={
                "image": ("test_image.jpg", image, "image/jpeg")
            }
        )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Mouse"
    assert data["category"] == "Electronics"
    assert data["price"] == 99.90
    assert "image" in data


def test_create_product_negative_price():
    with open("tests/test_image.jpg", "rb") as image:
        response = client.post(
            "/products",
            data={
                "name": "Mouse",
                "category": "Electronics",
                "price": "-10"
            },
            files={
                "image": ("test_image.jpg", image, "image/jpeg")
            }
        )

    assert response.status_code == 400
    assert response.json()["detail"] == "Price must be greater than 0."


def test_create_product_zero_price():
    with open("tests/test_image.jpg", "rb") as image:
        response = client.post(
            "/products",
            data={
                "name": "Mouse",
                "category": "Electronics",
                "price": "0"
            },
            files={
                "image": ("test_image.jpg", image, "image/jpeg")
            }
        )

    assert response.status_code == 400
    assert response.json()["detail"] == "Price must be greater than 0."


def test_create_product_blank_name():
    with open("tests/test_image.jpg", "rb") as image:
        response = client.post(
            "/products",
            data={
                "name": "     ",
                "category": "Electronics",
                "price": "10"
            },
            files={
                "image": ("test_image.jpg", image, "image/jpeg")
            }
        )

    assert response.status_code == 400
    assert response.json()["detail"] == "Name cannot be empty."


def test_create_product_blank_category():
    with open("tests/test_image.jpg", "rb") as image:
        response = client.post(
            "/products",
            data={
                "name": "Mouse",
                "category": "     ",
                "price": "10"
            },
            files={
                "image": ("test_image.jpg", image, "image/jpeg")
            }
        )

    assert response.status_code == 400
    assert response.json()["detail"] == "Category cannot be empty."


def test_list_products():
    response = client.get("/products")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_delete_nonexistent_product():
    response = client.delete("/products/9999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"