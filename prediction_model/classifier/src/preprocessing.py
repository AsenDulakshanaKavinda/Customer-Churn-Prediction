# Your explicit preprocessing functions / classes# Basic data loading or type parsing scripts

import pandas as pd
from pandas import DataFrame
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, OneHotEncoder

from utils import log, handle_errors

@handle_errors("preprocess dataframe", 1001)
def preprocess_dataframe(dataset: DataFrame) -> tuple[DataFrame, DataFrame, DataFrame, DataFrame]:
    columns = list(dataset.columns)
    
    if 'customerID' in columns:
        log.info("Dropping column: `customerID`")
        dataset.drop(columns='customerID', inplace=True)


    if 'TotalCharges' in columns:
        log.info("converting empty values in `TotalCharges` to 0")
        dataset["TotalCharges"] = dataset["TotalCharges"].replace(r'^\s*$', 0, regex=True)
        dataset["TotalCharges"] = pd.to_numeric(dataset['TotalCharges']).fillna(0)

    if 'Churn' in columns:
        log.info("Creating features and target dataframes")
        y = dataset['Churn']
        X = dataset.drop(columns='Churn')

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    log.info(f"X_train: {X_train.shape}, X_test: {X_test.shape}, y_train: {y_train.shape}, y_test: {y_test.shape}")

    return X_train, X_test, y_train, y_test


@handle_errors("feature preprocessing", 1001)
def feature_preprocessing(numerical_cols: list, categorical_cols: list) -> ColumnTransformer:
    
    log.info("creating - Feature preprocessing")
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', MinMaxScaler(), numerical_cols),
            ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_cols)
        ],
        remainder='passthrough'
    )
    return preprocessor


@handle_errors("encoding target", 1001)
def encode_target(y_train: DataFrame) -> DataFrame:
    log.info("Encode target separately")
    label_encoder = LabelEncoder()
    y_train_encoded = label_encoder.fit_transform(y_train).astype("float32")
    return y_train_encoded

