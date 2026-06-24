# Pure PyTorch nn.Module architecture

import torch
import torch.nn as nn


class ChurnClassifier(nn.Module):
    def __init__(
        self,
        input_dim: int = 46,
        hidden_dim_01: int = 64,
        hidden_dim_02: int = 128,
        hidden_dim_03: int = 64,
        hidden_dim_04: int = 32,
        output_dim: int = 1,
    ) -> None:
        super().__init__()

        self.net = nn.Sequential(
            # Input layer to first hidden layer
            nn.Linear(input_dim, hidden_dim_01),
            nn.ReLU(),
            # 1st hidden layer to 2nd hidden layer
            nn.Linear(hidden_dim_01, hidden_dim_02),
            nn.ReLU(),
            # 2nd hidden layer to 3rd hidden layer
            nn.Linear(hidden_dim_02, hidden_dim_03),
            nn.ReLU(),
            # 3rd hidden layer to 4th hidden layer
            nn.Linear(hidden_dim_03, hidden_dim_04),
            nn.ReLU(),
            # 4th hidden layer to 5th hidden layer
            nn.Linear(hidden_dim_04, output_dim),

        )

    def forward(self, X: torch.Tensor) -> torch.Tensor:
        return self.net(X.float())
