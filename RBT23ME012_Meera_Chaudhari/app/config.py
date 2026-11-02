import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Neon Database URL (strictly loaded from environment / .env, no hardcoded secrets)
DATABASE_URL = os.getenv("DATABASE_URL", "")

# Normalize SQLAlchemy URL for psycopg 3
if DATABASE_URL:
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+psycopg://", 1)
    elif DATABASE_URL.startswith("postgresql://") and not DATABASE_URL.startswith("postgresql+psycopg://"):
        DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg://", 1)

    # Remove channel_binding if present since standard sslmode handles Neon TLS cleanly
    if "&channel_binding=require" in DATABASE_URL:
        DATABASE_URL = DATABASE_URL.replace("&channel_binding=require", "")
    elif "?channel_binding=require&" in DATABASE_URL:
        DATABASE_URL = DATABASE_URL.replace("channel_binding=require&", "")
    elif "?channel_binding=require" in DATABASE_URL:
        DATABASE_URL = DATABASE_URL.replace("?channel_binding=require", "")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
PORT = int(os.getenv("PORT", 8000))
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
