# Library API

REST API built with FastAPI and SQLite for managing books. It supports creating, listing, retrieving, updating, deleting, and lending books.

## Technologies

* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn

## Project Structure

```
app/
├── main.py
├── database.py
├── models/
│   ├── libro_create.py
│   ├── libro_response.py
│   └── libro_db.py
├── routers/
│   └── libros.py
```

## Installation

1. Create virtual environment:

```
python -m venv .venv
```

2. Activate environment:

```
.venv\Scripts\activate
```

3. Install dependencies:

```
pip install fastapi uvicorn sqlalchemy
```

## Run the application

```
uvicorn app.main:app --reload
```

## API Documentation

Interactive docs available at:

```
http://127.0.0.1:8000/docs
```

## Endpoints

### Create book

POST /libros/

Creates a new book. Available copies are initialized equal to total copies.

### List books

GET /libros/

Returns all books.

### Get book by id

GET /libros/{id}

Returns a specific book.

* 404 if not found

### Update book

PUT /libros/{id}

Updates book data.

* 404 if not found
* 400 if total copies is less than borrowed copies

### Delete book

DELETE /libros/{id}

Deletes a book.

* 404 if not found

### Lend book

POST /libros/{id}/prestar

Decreases available copies by 1.

* 404 if not found
* 400 if no copies are available

## Example request

```
{
  "titulo": "1984",
  "autor": "George Orwell",
  "categoria": "Distopía",
  "anio_publicacion": 1949,
  "total_ejemplares": 5
}
```

## Notes

* Database is stored locally in libros.db
* No additional configuration required
* Designed for learning and testing purposes
