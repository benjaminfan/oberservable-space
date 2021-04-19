import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    DEVELOPMENT = True


class Mock(Config):
    USE_MONGO = False


class DB(Config):
    USE_MONGO = True
    DEVELOPMENT = False
    DEBUG = False
    MONGODB_SETTINGS = {
        'db': os.getenv('db'),
        'host': os.getenv('host'),
        'port': os.getenv('port'),
    }
