# config.py


class Config(object):
    DEBUG = False
    SECRET_KEY = 'u,fdP%6;[T$nXDd)qhpVM-TyQ,yZu8#]u:eYd~~eu7g`5tf'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BABEL_DEFAULT_LOCALE = 'it'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://scott:tiger@localhost/palmi'
