#!/bin/bash

# Run database migrations
python -c "from database.config import init_db; init_db()"

# Start the FastAPI application
uvicorn app.main:app --host 0.0.0.0 --port $PORT