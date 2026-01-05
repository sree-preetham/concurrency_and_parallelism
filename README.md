# Concurrency & Parallelism

This repository demonstrates in understanding concurrency in real world situations

The setup intentionally uses:
- **Docker only for the database + Adminer UI**
- **Python virtual environment (venv)** for running the application
- **No Docker for the Python app**

---

## Project Structure

```text
Concurrency_Parallelism/
├── db.py
├── docker-compose.yml
├── requirements.txt
├── Readme.md
├── venv/
└── threads/
    ├── __init__.py
    └── app.py
```

## Prerequisites

1. Python 3.9+ with Pip
2. Docker Desktop & Docker Compose
3. Git
4. Basic understanding of SQL and Python

## Database & Adminer Setup (Docker)
This project uses Docker only to run:

1. PostgreSQL
2. Adminer (A quick DB UI to visualize the data instead of CLI)

## Start the database and Adminer
From the project root:
```
docker-compose up -d
```

### This will start:
PostgreSQL on port 5432
Adminer UI on port 8080

### Access Adminer UI
Open your browser and go to:
```
http://localhost:8080
```
### Adminer Login Details
**System**	PostgreSQL
**Server**	postgres
**Username**	user
**Password**	password
**Database**	bank

Click Login.

## Create Database Schema
Once logged into Adminer click SQL command

Execute the following SQL
```
Create Table
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    balance INTEGER NOT NULL
);
```
```
Insert Initial Data
INSERT INTO accounts (username, balance)
VALUES ('luffy', 1000);
```
**Verify Data**
```
SELECT * FROM accounts;
```


You should see:

id	username	balance
1	luffy	1000

## Python Virtual Environment Setup

**From the project root:**

Create virtual environment (if not already created)
```python -m venv venv```

Activate the virtual environment
```source venv/bin/activate```

## Install Dependencies
```pip3 install -r requirements.txt```

## Database Connection Code (db.py)

The db.py file provides a reusable PostgreSQL connection used by all threads. This allows each thread to open its own DB connection.

## Application Code (threads/app.py)

Running the Application

⚠️ IMPORTANT: Always run the app from the project root.

From Concurrency_Parallelism/:

```
python3 -m threads.app
```

