
import os
import yaml
from pathlib import Path
from threading import Lock
from dotenv import load_dotenv; load_dotenv();
from pydantic import BaseModel
from .handle_exception import handle_errors
from .handle_logging import log

config_files = {
    "development": "config.dev.yaml",
    "production": "config.prod.yaml",
}

class TestModel(BaseModel):
    model_name: str
    model_path: str


class SystemConfig(BaseModel):
    test_model: TestModel


class ConfigLoader:
    _instrance = None
    _config = None
    _lock = Lock()

    def __new__(cls):
        if cls._instrance is None:
            with cls._lock:
                if cls._instrance is None:
                    cls._instrance = super().__new__(cls)
        return cls._instrance
    
    @handle_errors("load_config", 2001)
    def load_config(self) -> SystemConfig:

        if self._config is not None:
            return self._config
        
        app_env = os.getenv("APP_ENV", "development").lower()

        config_map = {
                "development": "config.dev.yaml",
                "production": "config.prod.yaml",
            }
        
        config_file = config_map.get(app_env)

        if config_file is None:
            log.warning(f"Unsupported APP_ENV: {app_env}")

        config_path = (
            Path(__file__).resolve().parent.parent
            / "config"
            / config_file
        )

        print(str(config_path))

        with open(config_path, "r") as file:
            raw_config = yaml.safe_load(file)
            print(raw_config)

        self._config = SystemConfig(**raw_config)

        log.info(f"Configuration loaded successfully from {config_file}")

        return self._config
    
    
config_loader = ConfigLoader()
sys_config = config_loader.load_config()      

        