from pydantic import BaseModel, Field

# ===========
# Data Models

class Product(BaseModel):
    id: int
    name: str = Field(min_length=1)
    category: str = Field(min_length=1)
    price: float = Field(gt=0)
    image: str

# ======================
# Product Creation Model

class ProductCreate(BaseModel):
    name: str = Field(min_length=1)
    category: str = Field(min_length=1)
    price: float = Field(gt=0)