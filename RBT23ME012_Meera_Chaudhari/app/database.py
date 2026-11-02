from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from .config import DATABASE_URL

# Fallback to local SQLite if DATABASE_URL is not set in environment
db_url = DATABASE_URL if DATABASE_URL else "sqlite:///./onyx_local.db"

engine_args = {"pool_pre_ping": True}
if "sqlite" not in db_url:
    engine_args.update({
        "pool_size": 5,
        "max_overflow": 10,
        "pool_recycle": 300
    })

engine = create_engine(db_url, **engine_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """Dependency that yields a database session for requests."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
