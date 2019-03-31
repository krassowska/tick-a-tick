from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ticks.db'
db = SQLAlchemy(app)

app.secret_key = 'ThisIsVerySecretKey'

import views
import models
import tweets