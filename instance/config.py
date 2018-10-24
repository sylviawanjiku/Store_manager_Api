import os

class Config(object):
    # class contains the general settings that we want all environments to have
    """Base configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    #  is a random string of characters that's used to generate hashes that secure various things in an app.
    SECRET = os.getenv('SECRET')


class DevelopmentConfig(Config):
    # tells the app to run under debugging mode when set to True
    """ Development configurations."""
    DEBUG = True

class TestingConfig(Config):
    """Testing configurations."""
    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    """Production configurations."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
secret_key = Config.SECRET
