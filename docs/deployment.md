# Deployment

## Docker

Start the full development stack:

```bash
docker compose up -d
```

Check services:

```bash
docker compose ps
```

Backend URL: `http://localhost:8000`

Frontend URL: `http://localhost`

## Database

Production should use PostgreSQL. In Docker compose the service name is `postgres`, not `localhost`.

```env
DATABASE_URL=postgresql+psycopg://USER:PASSWORD@postgres:5432/agentshield
```

## Render (or other cloud)

Deploy the FastAPI backend, PostgreSQL, and the React dashboard as separate services. Configure secrets via the platform’s environment variable UI. Never commit any credentials.
