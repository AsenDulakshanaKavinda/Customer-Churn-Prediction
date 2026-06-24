# Custom Skorch callbacks (like your MLflow logger)

from skorch.callbacks import Callback
import mlflow

class MLflowLoggerCallback(Callback):
    def on_epoch_end(self, net, **kwargs):
        # Get the history of the most recent epoch
        current_epoch_history = net.history[-1]
        epoch_num = current_epoch_history['epoch']

        # Extract losses (Skorch defaults: 'train_loss', 'valid_loss')
        mlflow.log_metric("train_loss", current_epoch_history['train_loss'], step=epoch_num)
        if 'valid_loss' in current_epoch_history:
            mlflow.log_metric("valid_loss", current_epoch_history['valid_loss'], step=epoch_num)
    