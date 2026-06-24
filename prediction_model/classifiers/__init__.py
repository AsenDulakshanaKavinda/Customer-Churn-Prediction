
import torch.nn as nn

class ChurnClassifier(nn.Module):
    def __init__(self, input_dim: int = 10, hidden_dim:int = 10) -> None:
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1)
        )

    def forward(self, X):
        return self.net(X.float())
