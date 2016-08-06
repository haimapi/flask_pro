class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    Debug = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///fk.db'
