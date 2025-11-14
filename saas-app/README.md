# Vivah Vows SaaS

Vivah Vows is a production-ready monorepo that bundles a Django + Django REST Framework backend with Channels-based chat and a modern React + Vite frontend. It unifies dating, astrology, wedding planning, finance, and subscription management workflows for a matrimonial SaaS platform.

## Project structure

```
saas-app/
  backend/
    backend/               # Django project configuration
    apps/                  # Modular domain apps
    manage.py
    requirements.txt
    Dockerfile
  frontend/
    src/                   # React application source
    package.json
    Dockerfile
  docker-compose.yml
  README.md
```

## Backend setup

1. Create and activate a virtual environment.
2. Install requirements:

   ```bash
   pip install -r backend/requirements.txt
   ```

3. Configure environment variables if needed (see `backend/backend/settings.py`).
4. Apply migrations and create a superuser:

   ```bash
   cd backend
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

### API highlights

- JWT authentication endpoints:
  - `POST /api/v1/auth/register`
  - `POST /api/v1/auth/login`
  - `POST /api/v1/auth/refresh`
- Domain endpoints are namespaced under `/api/v1/` (dating, astrology, wedding, finance, subscriptions, chat).
- WebSocket chat endpoint: `ws://localhost:8000/ws/chat/<thread_id>/` (authenticate with `?token=<JWT>` query parameter or `Authorization: Bearer <JWT>` header).

## Frontend setup

1. Install dependencies:

   ```bash
   cd frontend
   npm install
   ```

2. Start the Vite dev server:

   ```bash
   npm run dev
   ```

3. Access the app at [http://localhost:5173](http://localhost:5173).

The frontend integrates Redux Toolkit for state management, TailwindCSS for styling, Axios for API access, and a reusable WebSocket hook for live chat.

## Docker

The repository ships with Docker definitions for local development:

```bash
cd saas-app
docker-compose up --build
```

This starts PostgreSQL, the Django backend (on port 8000), and the React frontend (on port 5173).

## Admin access

Use the Django admin at `http://localhost:8000/admin/` with the superuser credentials you create. All domain entities are registered for quick inspection and management.

## Next steps

- Configure production-ready secrets and environment variables.
- Attach persistent storage for media uploads.
- Integrate a real email/SMS provider for OTP verification flows.
