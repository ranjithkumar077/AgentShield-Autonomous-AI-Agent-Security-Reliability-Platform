# Development

## Backend

```bash
cd backend
python -m venv venv
# Windows activation
.\\venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Frontend

```bash
cd frontend
npm install
npm run dev
```

## Tests

```bash
pytest -v
```

## Security Benchmark

```bash
python -m benchmarks.run_benchmark
```

## Adversarial Tests

```bash
python -m adversarial.run
```

## Performance Benchmark

```bash
python -m performance.benchmark
```

## Packaging

```bash
python -m build
```

## Code Quality

```bash
ruff check .
```
