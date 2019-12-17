from pathlib import Path


def get_ml_base_dir():
    return Path(__file__).resolve().parent


def get_model_dir():
    model_dir = get_ml_base_dir() / 'weights'
    model_dir.mkdir(parents=True, exist_ok=True)
    return model_dir
