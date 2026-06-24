from unittest.mock import MagicMock

import pytest

# import pandas as pd
from sqlalchemy import Engine

from data_pipeline.data_ingestion import DataIngestion


@pytest.fixture
def mock_engine():
    return MagicMock(spec=Engine)


@pytest.fixture
def sample_query():
    return "SELECT * FROM users"


def test_data_ingestion_initinalization(sample_query, mock_engine):
    ingestion = DataIngestion(query=sample_query, engine=mock_engine)

    assert ingestion.query == sample_query
    assert ingestion.engine == mock_engine
