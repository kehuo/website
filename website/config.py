class Config:
    pass


class TestConfig(Config):
    DEBUG = True
    SECRET_KEY = '123456'
    TESTING = True
    GUNICORN = False
    PORT = 5000


config = {
    'test': TestConfig,
}
