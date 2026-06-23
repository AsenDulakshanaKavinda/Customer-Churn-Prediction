from db_conn.db_manager import Base, DatabaseManager


def main():
    print("Hello from prediction-model!")

def init_db():
    db = DatabaseManager()
    # This looks at 'Base' and creates all tables that inherit from it
    Base.metadata.create_all(bind=db.engine)
    print("Tables created successfully!")

if __name__ == "__main__":
    init_db()
