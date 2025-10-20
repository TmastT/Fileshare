from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
DEBUG = os.getenv("DEBUG", "0").lower() in ("1", "true", "yes")
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or "sqlite:///" + str(BASE_DIR / "db.sqlite3")

# Change this file as necessary and rename to config.py
