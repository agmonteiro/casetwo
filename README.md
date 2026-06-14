Casetwo

## Running the application

Install the dependencies:

```
pip install -r requirements.txt
```

Start the FastAPI server:

```
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```

## Running the tests

Execute all tests:

```
pytest
```

Execute all tests with detailed output:

```
pytest -v
```

Execute only the integration tests:

```
pytest tests/test_api.py -v
```

Execute only the unit tests:

```
pytest tests/test_product_validation.py -v
```

The test suite should complete with all tests passing.

The tests are also executed automatically through the GitHub Actions workflow whenever code is pushed or a pull request is created.

The workflow can also be executed manually from the repository's Actions tab.
