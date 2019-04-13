from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_recaptcha import ReCaptcha
import sendgrid
import os



app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

app.config['RECAPTCHA_SITE_KEY'] = os.environ ['RECAPTCHA_SITE_KEY']
app.config['RECAPTCHA_SECRET_KEY'] = os.environ ['RECAPTCHA_SECRET_KEY']
recaptcha = ReCaptcha(app=app)

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))

import views
import models
import tweets