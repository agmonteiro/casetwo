from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .models import Product
from .storage import save_image

# ============
# Main Section

app = FastAPI()

app.mount(
    "/uploads",
    StaticFiles(directory="app/uploads"),
    name="uploads"
)

products: list[Product] = []
next_id = 1

# ==============
# API Protection

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================
# Product Creation

@app.post("/products")
async def create_product(
    name: str = Form(...),
    category: str = Form(...),
    price: float = Form(...),
    image: UploadFile = File(...)
):
    global next_id

    name = name.strip()
    category = category.strip()

    if not name:
        raise HTTPException(
            status_code=400,
            detail="Name cannot be empty."
        )

    if not category:
        raise HTTPException(
            status_code=400,
            detail="Category cannot be empty."
        )

    if price <= 0:
        raise HTTPException(
            status_code=400,
            detail="Price must be greater than 0."
        )

    image_path = await save_image(image)

    product = Product(
        id=next_id,
        name=name,
        category=category,
        price=price,
        image=image_path
    )

    products.append(product)
    next_id += 1

    return product

# ===============
# Product Listing

@app.get("/products")
def list_products():
    return products

# ==================
# Category Filtering

@app.get("/products/category/{category}")
def list_by_category(category: str):
    return [
        product
        for product in products
        if product.category.lower() == category.lower()
    ]

# ==================
# Product Alteration

@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    name: str,
    category: str,
    price: float
):
    name = name.strip()
    category = category.strip()

    if not name:
        raise HTTPException(
            status_code=400,
            detail="Name cannot be empty."
        )

    if not category:
        raise HTTPException(
            status_code=400,
            detail="Category cannot be empty."
        )

    if price <= 0:
        raise HTTPException(
            status_code=400,
            detail="Price must be greater than 0."
        )

    for product in products:
        if product.id == product_id:
            product.name = name
            product.category = category
            product.price = price
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )

# ================
# Product Deletion

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    global products

    for product in products:
        if product.id == product_id:
            products.remove(product)
            return {"message": "Deleted"}

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )