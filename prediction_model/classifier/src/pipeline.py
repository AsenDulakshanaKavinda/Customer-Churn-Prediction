# Assembles FunctionTransformer, Skorch, & Pipeline




from sklearn.compose import ColumnTransformer
from skorch import NeuralNetBinaryClassifier
from sklearn.pipeline import Pipeline
import torch
import torch.nn as nn

from classifier.src.models.churn_net import ChurnClassifier
from classifier.src.callbacks import MLflowLoggerCallback
from utils import log, handle_errors

@handle_errors("create pytorch skorch wrapper", 1001)
def create_pytorch_skorch_wrapper() -> NeuralNetBinaryClassifier:
    log.info("create pytorch skorch wrapper")
    pytorch_skorch_wrapper = NeuralNetBinaryClassifier(
        module = ChurnClassifier,
        module__input_dim = 46, # Passes this argument to ChurnClassifier's __init__
        criterion = nn.BCEWithLogitsLoss, # Standard loss for binary classification
        optimizer = torch.optim.Adam,
        lr = 0.001,
        max_epochs = 3,
        batch_size = 64,
        train_split = None, # Disables skorch's internal validation split if you want to use sklearn's
        callbacks=[('mlflow_logging', MLflowLoggerCallback())],
    )
    return pytorch_skorch_wrapper


@handle_errors("pipeline", 1001)
def pipeline(preprocessor: ColumnTransformer, nn_model: NeuralNetBinaryClassifier) -> Pipeline:
    log.info("creating pipeline")
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('nn_model', nn_model)
    ])
    return pipeline