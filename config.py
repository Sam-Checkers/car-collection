import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
class Config():

    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or '12345'
    SQLALCHEMY_DATABASE_URI = os.environ.get('postgresql://jjcuumbp:0ZzI8WrcGBRkUtNlmM8-ml4CkFWGB1KZ@salt.db.elephantsql.com/jjcuumbp')
    SQLALCHEMY_TRACK_NOTIFICAITONS = False