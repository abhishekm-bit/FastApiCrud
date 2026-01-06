# FastAPI MongoDB CRUD Application 🚀

This is a simple **CRUD (Create, Read, Update, Delete)** REST API built using **FastAPI** and **MongoDB**, running locally.

---

## 🛠 Tech Stack
- Python
- FastAPI
- MongoDB (Community Edition)
- Pydantic
- Uvicorn

---

## 📁 Project Structure
fastapi_mongo_crud/
├── main.py # FastAPI app entry point
├── routes.py # CRUD API routes
├── models.py # Pydantic data models
├── database.py # MongoDB connection
├── venv/ # Virtual environment


---

## ⚙️ Setup & Run (Local)

### 1️⃣ Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate

2️⃣ Install dependencies
pip install fastapi uvicorn pymongo

3️⃣ Start MongoDB

Ensure MongoDB service is running

Or open MongoDB Compass and connect to localhost:27017

4️⃣ Run the server
uvicorn main:app --reload

📘 API Documentation

FastAPI automatically provides API docs:

Swagger UI:
👉 http://127.0.0.1:8000/docs

---

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


Open frontend:

Double-click index.html

OR open it in any browser