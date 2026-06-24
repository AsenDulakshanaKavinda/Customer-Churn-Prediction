# Basic data loading or type parsing scripts

import pandas as pd
from pandas import DataFrame

from db_conn.db_manager import DatabaseManager
from utils import log, handle_errors

query = "SELECT * FROM telco_customer_churn" # load from config
database_manager = DatabaseManager()
engine = database_manager.engine

# 1. load dataset
@handle_errors("Load dataframe", 1001)
def load_dataframe() -> DataFrame:
    log.info("Loading dataframe from the Database")
    dataset = pd.read_sql(query, engine)
    log.info(f"Dataset loaded: {dataset.shape}")
    return dataset

