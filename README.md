# 📝 To-do FastAPI

A simple and lightweight **Todo REST API** built with **FastAPI** and **SQLite3**.

This project was created to practice backend fundamentals such as REST API, CRUD operations, Pydantic schemas, and SQLite database integration.


Create date: 08.08.2026
---

## 🚀 Features

* ✅ Create Todo
* 📋 Get all Todos
* ✏️ Update Todo
* 🗑️ Delete Todo
* 💾 SQLite3 database
* 🔄 REST API
* 📦 Pydantic data validation
* 📚 Automatic Swagger API documentation

---

## 🛠️ Tech Stack

| Technology   | Purpose                 |
| ------------ | ----------------------- |
| Python       | Programming language    |
| FastAPI      | REST API framework      |
| Uvicorn      | ASGI server             |
| SQLite3      | Database                |
| Pydantic     | Request data validation |
| Git / GitHub | Version control         |

---

## 📁 Project Structure

```text
to-do-project-v2/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routes.py
│
├── todo.db
├── requirements.txt
├── .gitignore
└── README.md
```

### 📌 File Responsibilities

| File               | Description                                    |
| ------------------ | ---------------------------------------------- |
| `main.py`          | FastAPI application and router configuration   |
| `database.py`      | SQLite connection and CRUD database operations |
| `schemas.py`       | Pydantic request schemas                       |
| `routes.py`        | API endpoints                                  |
| `models.py`        | Database model area                            |
| `requirements.txt` | Project dependencies                           |
| `.gitignore`       | Files ignored by Git                           |
| `todo.db`          | SQLite database                                |

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <https://github.com/javlonbeksaidov-developer/to-do-project-v2.git>
cd to-do-project-v2
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

**Windows — CMD:**

```bash
venv\Scripts\activate
```

**Windows — PowerShell:**

```bash
venv\Scripts\Activate.ps1
```

**Git Bash:**

```bash
source venv/Scripts/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

From the project root:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

You can test all CRUD operations directly from Swagger UI.

---

# 🔥 API Endpoints

## Get All Todos

```http
GET /todos
```

Returns all todos from the SQLite database.

### Example response

```json
[
    {
        "id": 1,
        "title": "Learn FastAPI",
        "description": "Practice CRUD",
        "status": false
    }
]
```

---

## Create Todo

```http
POST /todos
```

### Request body

```json
{
    "title": "Learn FastAPI",
    "description": "Build Todo API",
    "status": false
}
```

---

## Update Todo

```http
PUT /todos/{id}
```

Example:

```http
PUT /todos/1
```

### Request body

```json
{
    "title": "Learn FastAPI",
    "description": "Practice SQLite CRUD",
    "status": true
}
```

---

## Delete Todo

```http
DELETE /todos/{id}
```

Example:

```http
DELETE /todos/1
```

---

# 🔄 CRUD Architecture

```text
                Client
                  │
                  ▼
             FastAPI API
                  │
                  ▼
               routes.py
                  │
          ┌───────┴───────┐
          │               │
          ▼               ▼
      schemas.py      database.py
          │               │
          │               ▼
          │            SQLite3
          │               │
          └───────────────┘
                  │
                  ▼
               todo.db
```

---

# 🗄️ Database

The project uses **SQLite3**.

### Todo table

```sql
CREATE TABLE IF NOT EXISTS todo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100),
    description VARCHAR(255),
    status BOOLEAN DEFAULT FALSE
);
```

### Table structure

| Column        | Type         | Description            |
| ------------- | ------------ | ---------------------- |
| `id`          | INTEGER      | Unique Todo ID         |
| `title`       | VARCHAR(100) | Todo title             |
| `description` | VARCHAR(255) | Todo description       |
| `status`      | BOOLEAN      | Todo completion status |

---

## 👨‍💻 Author

**Javlonbek Saidov**

Python Backend Developer

GitHub: `javlonbeksaidov-developer`

---

⭐ If this project helped you learn FastAPI, consider giving it a star!
