from contextlib import contextmanager
from db_conn.db_manager import DatabaseManager

# A helper function to safely handle sessions
@contextmanager
def get_db_session():
    db = DatabaseManager()
    session = db.get_session()
    try:
        yield session
        session.commit()  # Automatically commit changes if no errors occur
    except Exception:
        session.rollback()  # Rollback if something goes wrong
        raise
    finally:
        session.close()  # Always close the session to prevent leaks
