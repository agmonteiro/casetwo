## Test Documentation

## Unit Tests

test_negative_price_rejected

Purpose:
Verify that Pydantic validation rejects products with a negative price.

Expected Result:
A ValidationError is raised.


test_zero_price_rejected

Purpose:
Verify that Pydantic validation rejects products with a price equal to zero.

Expected Result:
A ValidationError is raised.


test_valid_product

Purpose:
Verify that a valid product passes Pydantic validation.

Expected Result:
A ProductCreate object is created successfully and contains the expected values.

## Integration Tests

test_create_product_success

Purpose:
Verify that the API successfully creates a product when valid data is provided.

Expected Result:
The API returns HTTP 200 and the created product information.

test_create_product_negative_price

Purpose:
Verify that the API rejects products with negative prices.

Expected Result:
The API returns HTTP 400 with the message "Price must be greater than 0."

test_create_product_zero_price

Purpose:
Verify that the API rejects products with a price equal to zero.

Expected Result:
The API returns HTTP 400 with the message "Price must be greater than 0."

test_create_product_blank_name

Purpose:
Verify that the API rejects products whose name contains only whitespace.

Expected Result:
The API returns HTTP 400 with the message "Name cannot be empty."

test_create_product_blank_category

Purpose:
Verify that the API rejects products whose category contains only whitespace.

Expected Result:
The API returns HTTP 400 with the message "Category cannot be empty."

test_list_products

Purpose:
Verify that the product listing endpoint is accessible and returns a collection of products.

Expected Result:
The API returns HTTP 200 and a JSON array.

test_delete_nonexistent_product

Purpose:
Verify that the API properly handles attempts to delete a product that does not exist.

Expected Result:
The API returns HTTP 404 with the message "Product not found."
