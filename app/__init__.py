from fastapi import FastAPI
from routes.routes import register_routes
from fastapi.middleware.cors import CORSMiddleware
from database.config import init_db
import dotenv
import os

dotenv.load_dotenv()


DESCRIPITION =  """


---

## API Overview

The **Campaign manager backend API** provides a secure, scalable backend for managing campaigns, user authentication, and associated resources, built with **FastAPI** and **SQLAlchemy**.

### Key Features:

- ✅ **JWT-Based Authentication:** Uses clean PyJWT helpers with structured expiration (`exp`) for token-based authentication and role-based access control.
- ✅ **Structured JSON Responses:** Leverages `StandardMessageResponse` and `JsonWebTokenResponse` for consistent, documented API responses.
- ✅ **Clean Repository Structure:** Ready for collaboration with pre-configured environment management, CORS, and  - database connection scaffolding.
- ✅ **Scalable Endpoint Design:** Modular endpoints supporting clean query parameter parsing, middleware hooks, and future extension.
- ✅ **Developer-Friendly:** Automatic OpenAPI documentation (`/docs`) for exploring and testing endpoints during development.

---

### Example Auth Flow:

1. Client sends credentials to `/auth/login`.
2. Server authenticates user and returns a structured JWT response:

```json
{
    "token_string": "<JWT_TOKEN>",
    "exp": 1723423454,
    "roles": ["admin", "campaign_manager"]
}
```

3. Client stores the token and uses it in the `Authorization: Bearer <JWT_TOKEN>` header for protected routes.

---

### Planned Core Resources:

* Campaign management (create, update, delete campaigns)
* User management


---

### Authentication

All protected routes require a valid JWT token. Tokens expire after a configurable period (default 30 minutes) to enforce security best practices.

---

### Development Benefits:

✅ Allows your team to build a clean **Svelte, React, or Flutter frontend** on top of a secure, documented, scalable API.
✅ Easy to test locally with frontend dev servers (`localhost:5173` or configured `ALLOWED_ORIGIN`).

---

This backend is designed for **professional team collaboration**, fast iteration, and clean API delivery, while remaining flexible for scaling as your campaign management requirements grow.

---






"""




def create_app() -> FastAPI:
    app = FastAPI( title="Campaign Manager API",description=DESCRIPITION)
    ##init_db()

    app.add_middleware(
        CORSMiddleware,
        allow_origins = [str(os.getenv("ALLOWED_ORIGIN"))],
        allow_credentials=True,
        allow_methods = ["GET","POST","PUT","PATCH","DELETE"],
        allow_headers = ["*"],
    )


    register_routes(app=app)
    return app
