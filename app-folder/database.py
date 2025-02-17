import sqlite3
from datetime import datetime
import click
from flask import current_app, g

def get_database():
    if 'database' not in g:
        g.database = sqlite3.connect(current_app.config['DATABASE'], detect_types = sqlite3.PARSE_DECLTYPES)
        g.database.row_factory = sqlite3.Row
    return g.database

def close_db(e = None):
    db = g.pop('database', None)
    if db is not None:
        db.close()