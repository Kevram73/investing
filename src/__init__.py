from ast import Constant
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils.constants import Constants
from flask_bcrypt import Bcrypt
import os
from flask_migrate import Migrate

template_dir = os.path.abspath(Constants.FILE_FOLDER)
static_dir = os.path.abspath(Constants.STATIC_FOLDER)

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Constants.TRACK_MODIFICATIONS
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/invest'
app.config['SECRET_KEY'] = 'easyinvestment'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)


import routes