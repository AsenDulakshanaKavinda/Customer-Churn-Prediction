import torch
import torch.nn as nn


class ChurnClassifier(nn.Module):
    def __init__(
        self,
        input_dim_01: int = 32,
        hidden_dim_02: int = 64,
        hidden_dim_03: int = 32,
    ) -> None:
        super().__init__()

        self.net = nn.Sequential(
            # Input layer to first hidden layer
            nn.Linear(input_dim_01, hidden_dim_02),
            nn.ReLU(),
            # First hidden layer to second hidden layer
            nn.Linear(hidden_dim_02, hidden_dim_03),
            nn.ReLU(),
            # Second hidden layer to binary output (probability between 0 and 1)
            nn.Linear(hidden_dim_03, 1),
            nn.Sigmoid(),
        )

    def forward(self, X: torch.Tensor) -> torch.Tensor:
        return self.net(X.float())
