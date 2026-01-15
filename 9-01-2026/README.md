# 🚀 Training Syllabus Generation – EdTech (RAG Based)

AI-powered Training Syllabus Generator for EdTech domain using
Web-Augmented Generation (RAG) architecture.

This project scrapes real course data from URLs, converts it into embeddings, stores it in FAISS, retrieves relevant content, and generates professional syllabi using Gemini AI.


## 📌 Project Details

Domain: EdTech
Title: Training Syllabus Generation
Architecture: RAG (Retrieval Augmented Generation)
Backend Weightage: 70%
Frontend Weightage: 30%


# 🎯 Objective

To generate industry-aligned training syllabus by combining:
Real-world web data
Vector search (FAISS)
Gemini AI generation
Modern FastAPI backend
React + MUI frontend



# 🏗 Folder Structure
```
9-01-2026/
│
├── backend/
│   ├── api/
|        ├──auth.py
|        ├──syllabus.py  
│   ├── db/
|        ├──mongo.py
|        ├──vector_db.py  
│   ├── models/
|        ├──gemini_Model_Lists.py
|        ├──schemas.py  
│   ├── services/
│   │   ├── embeddings.py
│   │   ├── gemini.py
│   │   ├── rag.py
│   │   ├── scraper.py
│   │
│   ├── config.py
│   ├── main.py
│   ├── requirements.txt
│
├── frontend/
│   ├── node_modules/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   └── SyllabusForm.jsx
│   │   ├── redux/
│   │   │   ├── api.js
│   │   │   └── store.js
│   │   ├── App.js
│   │   ├── index.js
│
└── README.md
```

# ⚙ Tech Stack
## Backend

FastAPI
BeautifulSoup
FAISS
Gemini API
MongoDB

## Frontend
React
Material UI (MUI)
RTK Query
Redux Toolkit

# 🔄 Workflow (RAG Pipeline)
```
User enters URL
        ↓
Web scraping (BeautifulSoup)
        ↓
(Optional) Chunking
        ↓
Convert text → embeddings
        ↓
Normalize embeddings
        ↓
Store vectors in FAISS
        ↓
User query → embedding
        ↓
Normalize query vector
        ↓
Similarity search in FAISS
        ↓
Relevant context retrieved
        ↓
Context + prompt → Gemini AI
        ↓
Syllabus generated
        ↓
Response shown in frontend

```

# 🧠 Why URL is Used?

Provides real-world syllabus data
Improves accuracy
Makes output industry-relevant
Enables Web-Augmented Generation

# 🛠 Backend Setup

1 Create Virtual Environment

``` bash
python -m venv venv
venv\Scripts\activate
```

2 Create Virtual Environment
``` bash
python -m venv venv
venv\Scripts\activate
```

3️ Create .env / config
In backend/config.py
```bash
GEMINI_API_KEY="YOUR_API_KEY"
MONGO_URL="mongodb://localhost:27017"
```

4️ Run Backend
``` bash
uvicorn main:app --reload
```

Backend runs at:
``` bash
http://127.0.0.1:8000
```

Swagger:
``` bash
http://127.0.0.1:8000/docs
```

# 🎨 Frontend Setup
1️ Install Dependencies
``` bash
cd frontend
npm install
```

2️ Create .env
```bash
REACT_APP_API_URL=http://127.0.0.1:8000
```

3️ Start Frontend
```bash
npm start
```

Frontend runs at:
```bash
http://localhost:3000
```

# 🔥 API Endpoint

Generate syllabus

``` bash
POST /api/generate
```
Payload

```
{
  "url": "https://example.com/course",
  "course": "MERN Stack",
  "level": "Beginner",
  "duration": "1 Month"
}
```

# 🧪 Testing & Coverage Report

This project uses PyTest for backend testing and pytest-cov for coverage reporting.

## ✅ What is tested?
We currently test backend functionality only, including:
API endpoint working (/api/generate)
Web scraping logic
Embedding generation
FAISS vector storage & retrieval
RAG pipeline execution


# 📂 Test Files Location
```
backend/tests/
├── test_api.py
├── test_scraper.py
├── test_embeddings.py
├── test_rag.py

```
# ▶ Run Tests
``` bash
pytest
```

# 📊 Generate Coverage Report (Terminal)
```bash
pytest --cov=. --cov-report=term
```
# 🌐 Generate HTML Coverage Report
``` bash 
pytest --cov=. --cov-report=html
```
After running this command:
``` bash
backend/htmlcov/index.html
```
Open index.html in browser to view:

✔ File-wise coverage
✔ Percentage covered
✔ Highlighted lines (green/red)

index.html is the official coverage report.

# 📁 Save Coverage Output
``` bash
pytest --cov=. --cov-report=term > coverage.txt
```

```
🎯 Summary
Backend logic is fully tested
API integration tested
Coverage report generated using pytest-cov
HTML report available at htmlcov/index.html
```

# 🏆 Tools Used
```
PyTest
pytest-cov
FastAPI TestClient
```

# 🗃 FAISS Storage

Stores embeddings in-memory
Used for similarity search
Can be persisted if needed

# 📈 Features

✔ RAG Architecture
✔ Web scraping
✔ Vector similarity search
✔ Gemini prompt engineering
✔ MongoDB logging
✔ RTK Query
✔ Form validation
✔ Clean UI.



