.PHONY: db, delete, api, run-db

db:
	uv run -m backend.db

delete:
	rm -f scheduler.db

api:
	uv run fastapi dev backend/main.py

run-db:
	sqlite3 scheduler.db