import pytest
from pydantic import ValidationError

from app.models import ProductCreate

# ====================
# Test negative prices

def test_negative_price_rejected():
    with pytest.raises(ValidationError):
        ProductCreate(
            name="Mouse",
            category="Electronics",
            price=-10
        )

# =============
# Test 0 Prices

def test_zero_price_rejected():
    with pytest.raises(ValidationError):
        ProductCreate(
            name="Mouse",
            category="Electronics",
            price=0
        )

# ==================
# Test Valid Product

def test_valid_product():
    product = ProductCreate(
        name="Mouse",
        category="Electronics",
        price=149.90
    )

    assert product.name == "Mouse"
    assert product.category == "Electronics"
    assert product.price == 149.90