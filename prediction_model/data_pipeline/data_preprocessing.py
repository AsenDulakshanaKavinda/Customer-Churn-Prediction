import pandas as pd
from pandas import DataFrame
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, OneHotEncoder

from utils import handle_errors, log


class DataPreprocessing:
    def __init__(
        self, categorical_colms: list, numarical_colms: list, target_colm: str
    ):
        self.categorical_colms = categorical_colms
        self.numarical_colms = numarical_colms
        self.target_colm = target_colm

    # one hot encoding
    @handle_errors("one hot encoding", 20002)
    def one_hot_encoding(self, dataset: DataFrame) -> DataFrame:
        log.info("Performing one hot encoding")
        df_encoded = dataset.copy()
        ct = ColumnTransformer(
            transformers=[
                ("onehot", OneHotEncoder(sparse_output=False), self.categorical_colms)
            ],
            remainder='passthrough'
        )
        encoded_array = ct.fit_transform(df_encoded)
        rebuild_dataset = pd.DataFrame(
            encoded_array, columns=ct.get_feature_names_out()
        )

        # Clean up column names to look nicer (removes the 'onehot__' and 'remainder__' prefixes)
        rebuild_dataset.columns = rebuild_dataset.columns.str.replace(
            "onehot__", ""
        ).str.replace("remainder__", "")

        return rebuild_dataset

    # label encoding
    @handle_errors("label encoding", 20002)
    def label_encoding(self, dataset: DataFrame) -> DataFrame:
        log.info("Performing label encoding")
        df_encoded = dataset.copy()
        le = LabelEncoder()
        df_encoded[self.target_colm] = le.fit_transform(df_encoded[self.target_colm])

        return df_encoded

    # min max normalization
    @handle_errors("min max normalization", 20002)
    def min_max_normalization(self, dataset: DataFrame) -> DataFrame:
        log.info("Performing min max normalization on numerical columns")
        df_normalized = dataset.copy()

        if "TotalCharges" in list(df_normalized.columns):
            df_normalized["TotalCharges"] = pd.to_numeric(
                df_normalized["TotalCharges"].replace(" ", 0)
            )

        scaler = MinMaxScaler()
        # Scale only the specified numerical columns
        df_normalized[self.numarical_colms] = scaler.fit_transform(
            df_normalized[self.numarical_colms]
        )

        return df_normalized
