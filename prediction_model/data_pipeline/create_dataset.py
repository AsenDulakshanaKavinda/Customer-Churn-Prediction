# create dataset

import torch
from pandas import DataFrame
from torch.utils.data import Dataset

from utils import handle_errors


class ChurnDataset(Dataset):
    @handle_errors("Init churn dataset", 20004)
    def __init__(self, dataset: DataFrame, target_column: str) -> None:
        self.dataset = dataset
        self.X = self.dataset.drop(target_column).values
        self.y = self.dataset[target_column].values

    @handle_errors("Dataset length", 20004)
    def __len__(self):
        return len(self.dataset)

    @handle_errors("Get items from dataset", 20004)
    def __getitem__(self, index):
        features = torch.tensor(self.X[index], dtype=torch.float32)
        label = torch.tensor(self.y[index], dtype=torch.float32)
        return features, label
