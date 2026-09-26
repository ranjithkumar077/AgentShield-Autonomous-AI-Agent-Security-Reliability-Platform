# Getting Started

## Overview

AgentShield provides a security gateway for AI agents. This guide explains how to clone the repository, set up the development environment, and run the backend and frontend locally.

## Prerequisites

- Python 3.10+ (recommended 3.12)
- Node.js 18+
- Docker (optional for containerized deployment)

## Backend Setup

```bash
git clone https://github.com/ranjithkumar077/AgentShield.git
cd AgentShield/backend
python -m venv venv
# Windows PowerShell
.\\venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Frontend Setup

```bash
cd ../frontend
npm install
npm run dev
```

The dashboard will be served at `http://localhost:5173`.

## Running Benchmarks

```bash
cd ..
python -m benchmarks.run_benchmark
```

---
