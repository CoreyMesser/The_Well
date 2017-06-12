import os
from system_constants import SystemConstants


class Config(object):
    DATABASE_URI = os.environ.get(SystemConstants.DATABASE_URI)
    APP_NAME = 'The_Well'
    SECRET_KEY = 'dev_key'
    DEBUG = True
    SQLALCHEMY_ECHO = True
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    EXPLAIN_TEMPLATE_LOADING = False
    DATABASE = 'pb_db'

class FlaskConstants(object):
    HOST = "0.0.0.0"
    PORT = 8000
    DEBUG = True
