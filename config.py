import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')


class DevelopmentConfig(BaseConfig):
    DEVELOPMENT = True
    BCRYPT_LOG_ROUNDS = 4
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')


class ProductionConfig(BaseConfig):
    DEBUG = False
