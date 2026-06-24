import torch
from torch.utils.data import DataLoader, random_split

from utils import handle_errors, log

from .create_dataset import ChurnDataset


class CreateDataLoaders:
    @handle_errors("Init CreateDataLoaders", 20005)
    def __init__(self, dataset: ChurnDataset):
        self.data = dataset

    @handle_errors("create data loaders", 20005)
    def create_data_loaders(self):

        total_size = len(self.data)
        train_size = int(0.80 * total_size)
        val_size = int(0.10 * total_size)
        test_size = total_size - train_size - val_size

        log.info(
            f"Total: {total_size} | Train: {train_size} | Val: {val_size} | Test: {test_size}"
        )

        # Set seed for reproducible splits
        generator = torch.Generator().manual_seed(42)

        train_dataset, val_dataset, test_dataset = random_split(
            self.data, [train_size, val_size, test_size], generator=generator
        )

        # Create the DataLoader (e.g., batches of 32 rows, shuffled)
        train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
        val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)
        test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

        log.info("Created train, val and test data loaders")

        return (train_loader, val_loader, test_loader)
