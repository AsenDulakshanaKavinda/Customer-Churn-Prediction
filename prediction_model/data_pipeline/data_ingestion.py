import pandas as pd
from pandas import DataFrame
from sqlalchemy import Engine

from utils import handle_errors, log


class DataIngestion:
    def __init__(self, query: str, engine: Engine):
        self.query = query
        self.engine = engine

    @handle_errors("load dataset", 20001)
    def load_dataset(self) -> DataFrame:
        log.info("Loading dataset from the database")
        return pd.read_sql(self.query, self.engine)
