import os


class Config(object):
    pass

class ProdConfig(Config):
    pass


# config for development
class DevConfig(Config):
    Debug = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///fk.db'
    SECRET_KEY = 'you never guess'
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True

    # in windows terminal set MAIL_USERNAME=
    # in unix export MAIL_USERNAME=
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
