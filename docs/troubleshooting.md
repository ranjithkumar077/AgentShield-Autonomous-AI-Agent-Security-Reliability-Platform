# Troubleshooting

## Backend does not start

```bash
uvicorn app.main:app --reload
```

* Verify that the virtual environment is activated.
* Check that required environment variables are set (see `docs/configuration.md`).
* Review the console output for import errors.

## Database connection error

```env
DATABASE_URL=sqlite:///./agentshield.db   # Development
# or
DATABASE_URL=postgresql+psycopg://USER:PASSWORD@HOST:5432/agentshield   # Production
```

* For Docker, the hostname should be `postgres` (service name).
* Ensure the database container is running (`docker compose ps`).
* Test the connection manually:

```bash
psql $DATABASE_URL
```

## Frontend cannot reach backend

* Verify `VITE_API_URL` in `.env` of the frontend points to the correct backend URL.
* Ensure CORS settings in FastAPI allow the frontend origin.
* Test the health endpoint:

```bash
curl http://localhost:8000/health
```

## JWT authentication fails

* The `JWT_SECRET_KEY` used to sign tokens must be the same as the one configured in the backend.
* Tokens expire after `JWT_ACCESS_TOKEN_MINUTES`; obtain a fresh token.

## NVIDIA LLM requests fail

* Confirm `NVIDIA_API_KEY` is valid and not expired.
* Check network connectivity to `https://integrate.api.nvidia.com`.
* Review rate‑limit headers in the response.

## Docker issues

```bash
docker compose logs backend
```

* Look for missing environment variables or port conflicts.
* Recreate containers after changing `.env`:

```bash
docker compose down && docker compose up -d
```

## Migration issues

```bash
alembic upgrade head
```

* Ensure the `alembic.ini` file points to the correct database URL.
* If migrations fail, inspect the revision files in `backend/alembic/versions`.

## General tips

* Run `ruff check .` to catch lint errors.
* Use `git status` to ensure a clean working tree before committing.
* Keep secrets out of source control – never commit `.env` files.
