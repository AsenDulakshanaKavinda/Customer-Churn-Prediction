from db_conn.db_manager import DatabaseManager, Base
from db_conn.models import UserTest
from utils import log
from data_pipeline.pipeline import init_data_pipeline

def main():
    log.info("Hello from prediction-model!")



def init_db():
    # from db_conn.models import UserTest
    db = DatabaseManager()
    # This looks at 'Base' and creates all tables that inherit from it
    Base.metadata.create_all(bind=db.engine)
    print("Tables created successfully!")

if __name__ == "__main__":
    init_db()
    init_data_pipeline()
    main()
    
