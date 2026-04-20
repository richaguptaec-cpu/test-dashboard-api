# 🚀 Test Automation Results Dashboard API

## 📌 Overview

A RESTful API built using **FastAPI** to manage, store, and analyze test automation results.
This project simulates a real-world QA dashboard backend with filtering, reporting, and full CRUD operations.

---

## 🧱 Tech Stack

* Python 3.11+
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic (v2)
* Pytest

---

## ✨ Features

* ✅ Add test execution results
* ✅ Retrieve all results (filter by status, sort by latest, limit results)
* ✅ Get result by ID
* ✅ Update test results (partial update supported)
* ✅ Delete test results
* ✅ Summary report (pass/fail statistics)
* ✅ Input validation using Pydantic
* ✅ Timestamp tracking (UTC)
* ✅ Unit testing with Pytest

---

## 📂 Project Structure

```
test-dashboard-api/
│── app/
│   ├── main.py         # Entry Point
│   ├── routes.py       # API Endpoints
│   ├── models.py       # Database models
|   |── schemas.py      # Pydantic schemas
│   ├── database.py     # DB connection
│── tests/
│   └── test_api.py     # Unit tests
│── requirements.txt
│── README.md
```

---

## ▶️ How to Run Locally

### 1. Clone the repository

```
git clone https://github.com/richaguptaec-cpu/test-dashboard-api.git
cd test-dashboard-api
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the API

```
uvicorn app.main:app --reload
```

### 5. Open Swagger UI

http://127.0.0.1:8000/docs

---

## 📌 API Endpoints

| Method | Endpoint           | Description           |
| ------ | ------------------ | --------------------- |
| POST   | /test-results      | Add new test result   |
| GET    | /test-results      | Get all results       |
| GET    | /test-results/{id} | Get result by ID      |
| PUT    | /test-results/{id} | Update test result    |
| DELETE | /test-results/{id} | Delete test result    |
| GET    | /summary           | Get pass/fail summary |

---

## 🧪 Run Tests

```
pytest
```

---

## 📊 Sample Request

```
{
  "test_name": "login_test",
  "status": "PASS",
  "execution_time": 1.23,
  "environment": "staging"
}
```

---

## 🎯 Key Highlights

*   Designed RESTful APIs with input validation using Pydantic
*   Implemented full CRUD operations with proper error handling
*   Structured project with separation of concerns (routes,     models, schemas)
*   Built automated API tests using Pytest
*   Integrated SQLAlchemy ORM for database interactions
*   Developed a production-style backend structure

---

## 🚀 Future Improvements

* Docker support
* Authentication & authorization
* Pagination
* CI/CD pipeline

---

## 👤 Author

Richa Gupta
GitHub: https://github.com/richaguptaec-cpu/test-dashboard-api