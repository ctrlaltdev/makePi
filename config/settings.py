class BaseConfig():
   API_PREFIX = '/'
   TESTING = False
   DEBUG = False

class DevConfig(BaseConfig):
   FLASK_ENV = 'development'
   DEBUG = True

class ProductionConfig(BaseConfig):
   FLASK_ENV = 'production'

class TestConfig(BaseConfig):
   FLASK_ENV = 'development'
   TESTING = True
   DEBUG = True