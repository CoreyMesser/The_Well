import os
import sqlite3
from app import get_app

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from system_constants import SystemConstants
from config import Config
from flask import g
from flask_login import current_user


Base = declarative_base()
# Base.query = db_session.query_property()

app = get_app()
# config = Config()
# db_uri = os.environ.get(SystemConstants.DATABASE_URI)
engine = create_engine('postgresql://cmesser:Bedlum!1@localhost/pb_db')
db_session = sessionmaker(bind=engine)


@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = db_session()
    g.db.connect()
    g.user = current_user


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response
