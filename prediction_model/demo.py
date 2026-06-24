from classifier.src.data_utils import load_dataframe
from classifier.src.preprocessing import preprocess_dataframe, feature_preprocessing, encode_target
from classifier.src.pipeline import create_pytorch_skorch_wrapper, pipeline
from classifier.src.train import train_model

categorical_cols = [
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod",
]
numerical_cols = ["tenure", "MonthlyCharges", "TotalCharges"]
target_colm = "Churn"


dataframe = load_dataframe()

X_train, X_test, y_train, y_test = preprocess_dataframe(dataframe)
preprocessor = feature_preprocessing(numerical_cols, categorical_cols)
y_train_encoded = encode_target(y_train)

pytorch_skorch_wrapper = create_pytorch_skorch_wrapper()
pipeline = pipeline(preprocessor=preprocessor, nn_model=pytorch_skorch_wrapper)


train_model(experiment_name="first", pipeline=pipeline, X_train=X_train, y_train=y_train_encoded, X_test=X_test, y_test=y_test)



