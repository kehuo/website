class Config:
    pass


class TestConfig(Config):
    DEBUG = True
    SECRET_KEY = '123456'
    TESTING = True
    GUNICORN = False
    PORT = 5000
    TF_PREDICT_URL = 'http://localhost:8501/v1/models/{}:predict'


config = {
    'test': TestConfig,
}
