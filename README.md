# 🧠 AI Notes Generator API

An AI-powered backend application that generates **clear, structured notes** from text, files, or PDFs using **LLMs via OpenRouter**, built with **FastAPI**, **SQLModel**, and **PostgreSQL**.

---

## 🚀 Features

- 📝 Generate AI notes from text prompts
- 📄 Upload `.txt` files and summarize content
- 📕 Upload PDFs and extract text
- 🧠 Uses OpenRouter AI models for note generation
- 💾 Stores prompts and AI-generated notes in PostgreSQL
- ⚡ Async API calls for LLM inference
- 🧩 Clean modular backend architecture

---

## 🏗️ Tech Stack

- **Backend:** FastAPI  
- **Database:** PostgreSQL  
- **ORM:** SQLModel  
- **AI / LLM:** OpenRouter API  
- **HTTP Client:** httpx (async)  
- **File Processing:** pdfplumber  
- **Env Management:** python-dotenv  

---

## 📂 Project Structure

```text
.
├── main.py          # API routes (notes creation & retrieval)
├── database.py      # Database engine & session handling
├── model.py         # SQLModel table definitions
├── schema.py        # Request & response schemas
├── llm.py           # OpenRouter LLM integration
├── file.py          # File & PDF upload endpoints
├── .env             # Environment variables
├── requirements.txt
└── README.md
```

## Create a .env file in the root directory:

OPENROUTER_API_KEY=your_api_key_here
model=your_model_name_here

```bash
git clone https://github.com/IkkIsuhas/file_api.git
cd file_api
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Setup PostgreSQL or any other SQL(your choice)
Update the database URL in database.py

postgresql://postgres:password@localhost:5432/fastapi

## Run the application
```bash
uvicorn main:app --reload
```
API will be available at:

http://127.0.0.1:8000

Swagger UI:

http://127.0.0.1:8000/docs