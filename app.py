from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ticks.db'
db = SQLAlchemy(app)
port = int(os.environ.get('PORT', 5000))

app.secret_key = 'ThisIsVerySecretKey'

import views
import models
import tweets

app.run(host='0.0.0.0', port=port, debug=True)