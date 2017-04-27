import os
import sqlite3
from app import get_app

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# Base.query = db_session.query_property()

app = get_app()

class Database(object):
    def connect_db(self):
        """connect db"""
        rv = sqlite3.connect(app.config['DATABASE'])
        rv.row_factory = sqlite3.Row
        return rv


    def init_db(self):
        db = self.get_db()
        with app.open_resource('_database.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


    @app.cli.command('initdb')
    def initdb_command(self):
        """ini db"""
        self.init_db()
        print('Initialized the _database.')


    def get_db(self):
        """new db connect"""
        if not hasattr(g, 'sqlite_db'):
            g.sqlite_db = self.connect_db()
        return g.sqlite_db


    @app.teardown_appcontext
    def close_db(self, error):
        """closes db at end of request"""
        if hasattr(g, 'sqlite_db'):
            g.sqlite_db.close()
