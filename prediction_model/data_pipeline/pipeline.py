from .data_ingestion import DataIngestion
from .data_preprocessing import DataPreprocessing
from .create_dataset import ChurnDataset
from .create_dataloaders import CreateDataLoaders

from db_conn.db_manager import DatabaseManager

from utils import log, handle_errors

from data_pipeline import data_preprocessing



@handle_errors("init data pipeline", 20006)
def init_data_pipeline():
    # db
    database_manager = DatabaseManager()
    engine = database_manager.engine

    #  data ingestion
    query = "SELECT * FROM telco_customer_churn"
    data_ingestion = DataIngestion(query=query, engine=engine)
    dataset = data_ingestion.load_dataset()

    # data preprocesing
    categorical_colms = ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
       'PhoneService', 'MultipleLines', 'InternetService',
       'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
       'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
       'PaymentMethod']
    numarical_colms = ['tenure', 'MonthlyCharges', 'TotalCharges']
    target_colm= "Churn"
    data_preprocesing = DataPreprocessing(
        categorical_colms,
        numarical_colms,
        target_colm
    )

    ohe_dataset = data_preprocesing.one_hot_encoding(dataset)
    le_dataset = data_preprocesing.label_encoding(ohe_dataset)
    final_dataset = data_preprocesing.min_max_normalization(le_dataset)

    # 
    create_dataloaders = CreateDataLoaders(final_dataset)
    train, eval, test = create_dataloaders.create_data_loaders()



