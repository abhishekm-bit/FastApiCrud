# FastAPI MongoDB CRUD Application 🚀

This is a simple **CRUD (Create, Read, Update, Delete)** REST API built using **FastAPI** and **MongoDB**, running locally.

---

## 🛠 Tech Stack
- Python
- FastAPI
- MongoDB
- Pydantic
- Uvicorn
- Pytest

---

## 📁 Project Structure
```
Music
├── pytest.ini
├── Crud_FastApi/
│ ├── main.py
│ ├── routes.py
│ ├── models.py
│ ├── database.py
│ ├── tests/
│ │ └── test_users.py
│ └── venv/
└── frontend/
├── index.html
├── config.example.js

```

---
---

## ⚙️ Backend Setup & Run

``` bash
cd Crud_FastApi
```

``` bash
python -m venv venv
```

``` bash
venv\Scripts\activate
```

``` bash
pip install fastapi uvicorn pymongo pytest pytest-asyncio httpx
```

``` bash
cd ..
```

``` bash
uvicorn Crud_FastApi.main:app --reload
```

Swagger UI:
👉 http://127.0.0.1:8000/docs

---

``` bash 
cd Crud_FastApi
```

``` bash
venv\Scripts\activate
```

``` bash
cd ..
```

``` bash
pytest
```

## 🌐 Frontend (HTML + CSS + JavaScript)

This project also includes a **simple frontend UI** built using **HTML, CSS, and JavaScript** to interact with the FastAPI backend.

The frontend supports:
- Create User
- View All Users
- Update User by Email
- Delete User
- Client-side email validation
- Form auto-clear after operations

---
▶️ Run Frontend

Make sure backend is running:

uvicorn main:app --reload

1.Create frontend/config.js (do not commit):
``` bash
const API_URL = "Paste Backend Url heres";
```

2.Use config.example.js as reference

3.Open frontend/index.html in browser

##Features

Create / Read / Update / Delete Users

Email validation

FastAPI auto docs

Pytest async test cases

Clean project structure

