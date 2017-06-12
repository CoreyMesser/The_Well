import os

import logging
from config import Config
from system_constants import SystemConstants
import flask
from flask import Flask
from config import Config

_app_ = None


def get_app():
    global _app_
    if _app_ is None:
        config = Config()
        app = Flask(config.APP_NAME)
        app.config.from_object(config)
        _app_ = app
    return _app_

