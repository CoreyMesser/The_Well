import os

import logging

# import flask
# from flask import Flask

_app_ = None

def get_app():
    global _app_
    if _app_ is None:
        app = __name__
        # app.config.update(dict(
        #     DATABASE=os.path.join(app.root_path, 'PB_DB.sqlite'),
        #     SECRET_KEY='dev_key',
        # ))
        # app.config.from_envvar('PB', silent=True)
        _app_ = app
    return _app_

