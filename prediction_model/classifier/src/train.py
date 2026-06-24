import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature
from pandas import DataFrame
from sklearn.pipeline import Pipeline

from utils import log, handle_errors

@handle_errors("train_model", 1001)
def train_model(
        experiment_name: str, 
        pipeline: Pipeline,
        X_train: DataFrame, y_train: DataFrame, X_test: DataFrame, y_test: DataFrame, 
):

    # 1. Define a name for your registered model in the registry
    model_registry_name = "customer_churn_model"

    # 2. Set your MLflow experiment
    mlflow.set_experiment(experiment_name=experiment_name)

    mlflow.end_run()

    with mlflow.start_run() as run:
        # Train your Scikit-Learn/Skorch pipeline
        pipeline.fit(X_train, y_train)
        
        # Infer the input/output schema (Signature)
        # This prevents bad data shapes in production later
        predictions_example = pipeline.predict(X_test[:5])
        signature = infer_signature(X_test, predictions_example)
        
        # Log the pipeline AND register it at the same time
        mlflow.sklearn.log_model(
            sk_model=pipeline,
            artifact_path="model",
            signature=signature,
            input_example=X_test[:1], # Optional: helps document the schema in the UI
            registered_model_name=model_registry_name , # <-- This registers it!
            # skops_trusted_types=True
            serialization_format="cloudpickle"
        )
        
        log.info(f"Model successfully registered under name: '{model_registry_name}'")